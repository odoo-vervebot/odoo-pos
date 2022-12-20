odoo.define('point_of_sale.ScaleScreen', function(require) {
    'use strict';

    const { useState, useExternalListener } = owl.hooks;
    const PosComponent = require('point_of_sale.PosComponent');
    const { round_precision: round_pr } = require('web.utils');
    const Registries = require('point_of_sale.Registries');
    const ProductScreen = require('point_of_sale.ProductScreen');
    var weight_scale_refreshId = null;

    class ScaleScreen extends PosComponent {
        /**
         * @param {Object} props
         * @param {Object} props.product The product to weight.
         * @param {Object} props.clickonproduct The product to weight.
         */
        constructor() {
            super(...arguments);
            useExternalListener(document, 'keyup', this._onHotkeys);
            this.state = useState({ weight: 0, weightScreen: this.props.clickonproduct, refreshIntervalId: ""  });
            this.setWeight(true);
            this.start_barcode = new ProductScreen();
            this.start_barcode._stopcustomBarcodeScanner();
        }
        mounted() {
            // start the scale reading
            this._readScale();
        }
        willUnmount() {
            // stop the scale reading
            this.env.pos.proxy_queue.clear();
        }
        back() {
            this.props.resolve({ confirmed: false, payload: null });
            this.trigger('close-temp-screen');
             // Modified by : jaswant
             this._stopcustomWeightScanner();
             this.start_barcode._ConnectBarcodeDevice(true);
            // this.setWeight(false);
            // this.state.weightScreen = false;
            // clearInterval(this.state.refreshIntervalId);
        }
        confirm() {
            this.props.resolve({
                confirmed: true,
                payload: { weight: this.state.weight },
            });
            // Modified by : jaswant
            this._stopcustomWeightScanner();
            this.start_barcode._ConnectBarcodeDevice(true);
            this.trigger('close-temp-screen');
            // this.setWeight(false);
        }
        _onHotkeys(event) {
            if (event.key === 'Escape') {
                this.back();
            } else if (event.key === 'Enter') {
                this.confirm();
            }
            this.setWeight(false);
        }
        _readScale() {
            this.env.pos.proxy_queue.schedule(this._setWeight.bind(this), {
                duration: 500,
                repeat: true,
            });
        }
        async _setWeight() {
            const reading = await this.env.pos.proxy.scale_read();
            this.state.weight = reading.weight;
        }
        _stopcustomWeightScanner() {
            clearInterval(weight_scale_refreshId);
        }
        async setWeight(params) {
            let weightScreen=true
           
            this.state.weightScreen = params
            
            // this.state.weightScreen = params
            const fetchWeightFromServer = async () => {
                
                console.log("this.state.weightScreen : ", this.state.weightScreen)
                console.log("this.props.clickonproduct : ", this.props.clickonproduct)

                if (this.state.weightScreen) {

                    var tempWeight = 0;

                    //    await fetch("https://eq9hczw3pc.execute-api.us-west-2.amazonaws.com/default/weightscale").then(function (response) {
                    //         return response.text();
                    //     }).then(function (data) {
                    //         console.log(data);
                    //         console.log(JSON.parse(data));
                    //         let tempWeightData = JSON.parse(data)
                    //         console.log(parseFloat(tempWeightData));
                    //         console.log(Number(tempWeightData));
                    //         // this.state.weightInput=tempWeightData;
                    //         tempWeight = parseFloat(tempWeightData);

                    //         console.log("inner_tempWeight : ", tempWeight);
                    //     })


                    let headersList = {
                        "Accept": "*/*",
                        // "User-Agent": "Thunder Client (https://www.thunderclient.com)",
                        "Access-Control-Allow-Headers": "*",
                        "Access-Control-Allow-Methods": "*",
                        "Access-Control-Allow-Origin": "*",
                        "Content-Type": "application/json"
                    }

                    // var myHeaders = new Headers();
                    // myHeaders.append("Content-Type", "application/json");

                    let bodyContent = JSON.stringify({
                        weight: "",
                        callFrom: "FromOdoo"
                    });
                    // await fetch("https://74w06xmpe9.execute-api.us-west-2.amazonaws.com/default/weightscale_post", {
                    //     method: "POST",
                    // body: bodyContent,

                    let scale_url = this.env.pos.db.get_scale_url();
                    await fetch(scale_url, {
                        method: "GET",                   
                        headers: headersList
                    }).then(function (response) {
                        return response.text();
                    }).then(function (data) {
                        console.log("data : ", data);
                        console.log(JSON.parse(data));
                        let tempWeightData = JSON.parse(data).weight.replace(/(\r\n|\n|\r)/gm, "")
                        if (tempWeightData.includes(' lb.'))
                        {
                            console.log("data from API");
                            if(!isNaN(parseFloat(tempWeightData.split(' ')[0]))) {
                                // is float    
                            console.log(parseFloat(tempWeightData));
                            console.log(Number(tempWeightData));
                            // this.state.weightInput=tempWeightData;
                            tempWeight = parseFloat(tempWeightData);

                            console.log("inner_tempWeight : ", tempWeight);
                        }
                        else{
                            
                            if(weightScreen){
                                alert(tempWeightData);
                                weightScreen=false;
                            }
                            
                        }
                    }
                    })



                    // var weightInKg = parse.float(this.state.weightInput);

                    console.log("outside_tempWeight : ", tempWeight);
                    console.log("outside_weightInput : ",this.state.weightInput);
                    var weightInKg = tempWeight;

                    if (!isNaN(weightInKg)) {
                        console.log("weightInKg : ", weightInKg);
                        this.env.pos.proxy.debug_set_weight(weightInKg);
                    }

                }
            }

            // if (this.state.weightScreen) {
                // setInterval(fetchWeightFromServer, 400)
                clearInterval(weight_scale_refreshId);
                weight_scale_refreshId = setInterval(fetchWeightFromServer, 200)
                // this.state.refreshIntervalId = setInterval(fetchWeightFromServer, 400)
                // console.log("this.state.refreshIntervalId : ", this.state.refreshIntervalId)
            // } else {
            //     clearInterval(refreshIntervalId);
            // }

        }
        get _activePricelist() {
            const current_order = this.env.pos.get_order();
            let current_pricelist = this.env.pos.default_pricelist;
            if (current_order) {
                current_pricelist = current_order.pricelist;
            }
            return current_pricelist;
        }
        get productWeightString() {
            const defaultstr = (this.state.weight || 0).toFixed(3) + ' Kg';
            if (!this.props.product || !this.env.pos) {
                return defaultstr;
            }
            const unit_id = this.props.product.uom_id;
            if (!unit_id) {
                return defaultstr;
            }
            const unit = this.env.pos.units_by_id[unit_id[0]];
            const weight = round_pr(this.state.weight || 0, unit.rounding);
            let weightstr = weight.toFixed(Math.ceil(Math.log(1.0 / unit.rounding) / Math.log(10)));
            weightstr += ' ' + unit.name;
            return weightstr;
        }
        get computedPriceString() {
            return this.env.pos.format_currency(this.productPrice * this.state.weight);
        }
        get productPrice() {
            const product = this.props.product;
            return (product ? product.get_price(this._activePricelist, this.state.weight) : 0) || 0;
        }
        get productName() {
            return (
                (this.props.product ? this.props.product.display_name : undefined) ||
                'Unnamed Product'
            );
        }
        get productUom() {
            return this.props.product
                ? this.env.pos.units_by_id[this.props.product.uom_id[0]].name
                : '';
        }
    }
    ScaleScreen.template = 'ScaleScreen';

    Registries.Component.add(ScaleScreen);

    return ScaleScreen;
});

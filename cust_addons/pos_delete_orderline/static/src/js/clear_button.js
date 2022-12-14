odoo.define('pos_delete_orderline.DeleteOrderLinesAll', function(require) {
'use strict';
   const { Gui } = require('point_of_sale.Gui');
   const PosComponent = require('point_of_sale.PosComponent');
   const { posbus } = require('point_of_sale.utils');
   const ProductScreen = require('point_of_sale.ProductScreen');
   const { useListener } = require('web.custom_hooks');
   const Registries = require('point_of_sale.Registries');
   const PaymentScreen = require('point_of_sale.PaymentScreen');
   class OrderLineClearALL extends PosComponent {
       constructor() {
           super(...arguments);
           useListener('click', this.onClick);
       }
       _exportUnpaidOrders(){
        // get cart item from local storage
        // process
        // post   
        let unpaid_key = null
        for (var key in localStorage){
            let str = key;
            let target = "_unpaid_orders";
            var last  = str.substring(str.length-(target.length));
            if (last == target ){
                unpaid_key = str;
            }
            // console.log(key)
         }

        let product_data = localStorage.getItem(unpaid_key)
        // console.log("product_data ", product_data)
        let json_data = JSON.parse(product_data)
        let os = json_data[0].data
        var myHeaders = new Headers();
        myHeaders.append("Content-Type", "application/json");
        
        var raw = JSON.stringify({
        'data': os
        });

        var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
        };

        fetch("http://127.0.0.1:5000/product/", requestOptions)
        .then(response => response.text())
        .then(result => console.log(result))
        .catch(error => console.log('error', error));

    }
      async onClick() {
                const { confirmed} = await this.showPopup("ConfirmPopup", {
                       title: this.env._t('Clear Orders?'),
                       body: this.env._t('Are you sure you want to delete all orders from the cart?'),
                   });
                if(confirmed){

                    const order = this.env.pos.get_order();
                    order.remove_orderline(order.get_orderlines());
                    // _exportUnpaidOrders();
                    let unpaid_key = null
                    for (var key in localStorage){
                        let str = key;
                        let target = "_unpaid_orders";
                        var last  = str.substring(str.length-(target.length));
                        if (last == target ){
                            unpaid_key = str;
                        }
                        // console.log(key)
                     }
            
                    let product_data = localStorage.getItem(unpaid_key)
                    // console.log("product_data ", product_data)
                    let json_data = JSON.parse(product_data)
                    let os = json_data[0].data
                    var myHeaders = new Headers();
                    myHeaders.append("Content-Type", "application/json");
                    
                    var raw = JSON.stringify({
                    'data': os
                    });
            
                    var requestOptions = {
                    method: 'POST',
                    headers: myHeaders,
                    body: raw,
                    redirect: 'follow'
                    };
            
                    fetch("http://127.0.0.1:5000/product/", requestOptions)
                    .then(response => response.text())
                    .then(result => console.log(result))
                    .catch(error => console.log('error', error));
                }
       }

   }

   OrderLineClearALL.template = 'OrderLineClearALL';
   ProductScreen.addControlButton({
       component: OrderLineClearALL,
       condition: function() {
           return this.env.pos;
       },
   });
   Registries.Component.add(OrderLineClearALL);
   return OrderLineClearALL;
});
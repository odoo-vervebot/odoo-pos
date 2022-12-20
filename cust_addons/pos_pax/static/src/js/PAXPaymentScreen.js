odoo.define('pos_pax.PAXPaymentScreen', function (require) {
    'use strict';

    // Part of Hibou Suite Professional. See LICENSE_PROFESSIONAL file for full copyright and licensing details.

    const { _t } = require('web.core');
    const PaymentScreen = require('point_of_sale.PaymentScreen');
    const Registries = require('point_of_sale.Registries');
    const { useListener } = require('web.custom_hooks');
    const PAX = require('pos_pax.pax_device');

    PAX.mDestinationIP = '';

    const PAXPaymentScreen = (PaymentScreen) =>
        class extends PaymentScreen {
            constructor() {
                super(...arguments);
                // tempting to use 'send-payment-request',
                // but method implements things that don't seem to exist yet (payment_method.payment_terminal)
                useListener('pax-send-payment-request', this._sendPAXPaymentRequest);
                useListener('pax-send-payment-request-debit', this._sendPAXPaymentRequestDebit);
            }

            async _sendPAXPaymentRequest({ detail: line }) {
                this.pax_credit_transaction(line, 'credit');
            }

            async _sendPAXPaymentRequestDebit({ detail: line }) {
                this.pax_credit_transaction(line, 'debit');
            }

            print_clover(){
                // validateOrder()
                alert("payment successfully done");
                this.validateOrder(false);
                var printHeaders = new Headers();
                printHeaders.append("X-Clover-Device-Id", "C132UQ20330635");
                printHeaders.append("X-POS-ID", "Vervebot ");
                printHeaders.append("Authorization", "Bearer e633a51a-2cd2-608e-15d2-d374176e449a");
                printHeaders.append("Content-Type", "application/json");



                var raw = JSON.stringify({
                "printdeviceId": "{{printerid}}",
                "text": [
                    "SANDBOX SUPPLIES",
                    "415 N Mathilda Ave",
                    "Sunnyvale, CA 94085",
                    "Mon Dec 19 2022 05:31:50 GMT+0530 (India Standard Time)",
                    "",
                    "Order number: ",
                    "Items:",
                    "1 shovel @ $29.00",
                    "20 lbs sand @ $0.69/lb",
                    "",
                    "Subtotal: 42.80",
                    "Tax: 3.42",
                    "Total: 46.22",
                    "",
                    "Please sign below",
                    "",
                    "________________________",
                    "",
                    "",
                    "I agree to pay the above total amount according to my card issuer agreement.",
                    "",
                    ""
                ]
                });

                var printrequestOptions = {
                method: 'POST',
                headers: printHeaders,
                body: raw,
                redirect: 'follow'
                };

                fetch("https://sandbox.dev.clover.com/connect/v1/device/print/text", printrequestOptions)
                .then(response => response.text())
                .then(result => console.log(result))
                .catch(error => console.log('error', error));
            }

            pax_credit_transaction(line, tender_type) {
                var order = this.env.pos.get_order();
                
                // if(this.env.pos.getPAXOnlinePaymentJournals().length === 0) {
                //     return;
                // }

                var self = this;
                var transaction = {};

                var purchase_amount = line.get_amount();

                var transactionType = '01';  // SALE
                if (purchase_amount < 0.0) {
                    purchase_amount = -purchase_amount;
                    transactionType = '02';  // RETURN
                }

                transaction = {
                    command: (tender_type == 'debit') ? 'T02' : 'T00',
                    version: '1.28',
                    transactionType: transactionType,
                    amountInformation: {
                        TransactionAmount: (purchase_amount * 100) | 0,  // cast to integer
                    },
                    cashierInformation: {
                        ClerkID: this.env.pos.user.name,
                    },
                    traceInformation: {
                        ReferenceNumber: self.env.pos.get_order().uid,
                        // InvoiceNumber: self.env.pos.get_order().uid,
                    },
                }

                var def = new $.Deferred();

                // show the transaction popup.
                // the transaction deferred is used to update transaction status
                self.showPopup('PAXPaymentTransactionPopup', {
                    transaction: def
                });
                def.notify({
                    message: _t('Handling transaction...'),
                });



                var myHeaders = new Headers();
                myHeaders.append("X-Clover-Device-Id", "C132UQ20330635");
                myHeaders.append("X-POS-ID", "Vervebot");
                myHeaders.append("Content-Type", "application/json");
                myHeaders.append("Authorization", "Bearer  e633a51a-2cd2-608e-15d2-d374176e449a");

                var raw = JSON.stringify({});

                var requestOptions = {
                method: 'POST',
                headers: myHeaders,
                body: raw,
                redirect: 'follow'
                };

                fetch("https://sandbox.dev.clover.com/connect/v1/device/ping", requestOptions)
                .then(response => response.text())
                .then(result => console.log(result))
                .catch(error => console.log('error', error));

                

                var paymentHeaders = new Headers();
                paymentHeaders.append("X-Clover-Device-Id", "C132UQ20330635");
                paymentHeaders.append("X-POS-ID", "Vervebot ");
                paymentHeaders.append("Idempotency-Key", "d68fd10a-14af-4bd8-b25d-7cc8dc972512");
                paymentHeaders.append("Content-Type", "application/json");
                paymentHeaders.append("Authorization", "Bearer e633a51a-2cd2-608e-15d2-d374176e449a");
                console.log("amount  ", purchase_amount * 100)
                console.log("externalPaymentId  ", order.uid)
                var raw = JSON.stringify({
                "amount": purchase_amount * 100,
                "final": true,
                "externalPaymentId": order.uid
                });

                var paymentrequestOptions = {
                method: 'POST',
                headers: paymentHeaders,
                body: raw,
                redirect: 'follow'
                };

                fetch("https://sandbox.dev.clover.com/connect/v1/payments", paymentrequestOptions)
                .then(response => response.text())
                .then(
                    result => result.status != 200 ? this.print_clover() :console.log(result)).catch(
                    error => console.log('error', error)
                    );


              
                
                // var myHeaders = new Headers();
                // myHeaders.append("Content-Type", "application/json");
                // myHeaders.append("X-POS-ID", "Vervebot");
                // myHeaders.append("X-Clover-Device-Id", "C132UQ20330635");
                // myHeaders.append("Access-Control-Allow-Origin", '*');
                // myHeaders.append("Access-Control-Allow-Headers", 'Content-Type');
                // myHeaders.append("Access-Control-Allow-Credentials", true);
                

                // var requestOptions = {
                //     method: 'GET',
                //     headers: myHeaders,
                // };

                // let mDestinationIP = "https://sandbox.dev.clover.com/v1/device/ping/";

                // fetch(mDestinationIP, requestOptions)
                // .then(response => response.text())
                // .then(result => console.log(result))
                // .catch(error => console.log('error', error));

                // PAX.mDestinationIP = self.env.pos.config.pax_endpoint;
                // PAX[(tender_type == 'debit') ? 'DoDebit' : 'DoCredit'](transaction, function (response) {
                //     console.log(response);
                //     var parsed_response = self.env.pos.decodePAXResponse(response);
                //     if (parsed_response.fail) {
                //         def.resolve({message: parsed_response.fail})
                //         return;
                //     }
                //     if (parsed_response.success) {
                //         line.paid = true;
                //         line.pax_card_number = parsed_response.card_num;
                //         line.pax_txn_id = parsed_response.txn_id;
                //         line.pax_approval = parsed_response.approval;
                //         line.pax_txn_pending = false;
                //         line.pax_tender_type = tender_type;
                //         line.set_credit_card_name();
                //         order.trigger('change', order);
                //         self.render();
                //         def.resolve({message: 'Approval ' + parsed_response.approval, auto_close: true})
                //     }
                //     def.resolve({message: _t('Unknown response.')})
                // }, function (fail){
                //     def.resolve({message: _t('Communication Failure: ') + fail});
                // });
            }

            pax_do_reversal(line) {
                var def = new $.Deferred();
                var self = this;
                var transaction = {};

                // show the transaction popup.
                // the transaction deferred is used to update transaction status
                this.showPopup('PAXPaymentTransactionPopup', {
                    transaction: def
                });
                def.notify({
                    message: 'Sending reversal...',
                });

                transaction = {
                    command: (line.pax_tender_type == 'debit') ? 'T02' : 'T00',
                    version: '1.28',
                    transactionType: (line.get_amount() > 0) ? '17' : '18',  // V/SALE, V/RETURN
                    cashierInformation: {
                        ClerkID: this.env.pos.user.name,
                    },
                    traceInformation: {
                        ReferenceNumber: this.env.pos.get_order().uid,
                        InvoiceNumber: '',
                        AuthCode: line.pax_approval,
                        TransactionNumber: line.pax_txn_id,
                    },
                }

                PAX.mDestinationIP = self.env.pos.config.pax_endpoint;
                PAX[(line.pax_tender_type == 'debit') ? 'DoDebit' : 'DoCredit'](transaction, function (response) {
                    var parsed_response = self.env.pos.decodePAXResponse(response);
                    if (parsed_response.fail) {
                        def.resolve({message: parsed_response.fail})
                        return;
                    }
                    if (parsed_response.success) {
                        def.resolve({
                            message: _t('Reversal succeeded.'),
                            auto_close: true,
                        });
                        self.remove_paymentline_by_ref(line);
                        return;
                    }
                    def.resolve({message: _t('Unknown response.')})
                }, function (fail){
                    def.resolve({message: _t('Communication Failure: ') + fail});
                });
            }

            remove_paymentline_by_ref(line) {
                this.env.pos.get_order().remove_paymentline(line);
                this.render();
            }

            /**
             * @override
             */
            deletePaymentLine(event) {
                const { cid } = event.detail;
                const line = this.paymentLines.find((line) => line.cid === cid);
                if (line.pax_txn_id) {
                    this.pax_do_reversal(line);
                } else {
                    super.deletePaymentLine(event);
                }
            }

            /**
             * @override
             */
             async validateOrder(isForceValidate) {
                const res = super.validateOrder(...arguments);
                console.log("validated")
                
            }
           
            addNewPaymentLine({ detail: paymentMethod }) {
                
                const order = this.env.pos.get_order()
                const res = super.addNewPaymentLine(...arguments);
                if (res && paymentMethod.use_payment_terminal == 'pax') {
                    // alert("pax payment line alert");
                    order.selected_paymentline.pax_txn_pending = true;
                    let line = order.selected_paymentline;
                    console.log(order.selected_paymentline);
                    order.trigger('change', order);
                    this.pax_credit_transaction(line,"credit");
                    this.render();
                }
            }

        };

    Registries.Component.extend(PaymentScreen, PAXPaymentScreen);

    return PAXPaymentScreen;
});

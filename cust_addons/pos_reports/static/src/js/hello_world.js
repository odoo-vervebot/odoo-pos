
// odoo.define('hello_world.main', function (require) {  const AbstractAction = require('web.AbstractAction');  console.log(AbstractAction);});
odoo.define('hello_world.main',
    function (require) {
    const AbstractAction = require('web.AbstractAction');
    const core = require('web.core');
    var rpc = require('web.rpc');
    const { useState, onMounted } = owl.hooks;
    // const { Component, mount, xml, useState, onWillRender, onPatched} = owl;
    var model = 'product.product';
    const QWeb = core.qweb;

    // Use an empty array to search for all the records
    var domain = [];
    // Use an empty array to read all the fields of the records
    var fields = ['id','barcode','name'];
    //'product.product', 'search_read', [[['product_variant_count', '=', True]]], {'fields': ['barcode', 'name', 'list_price', 'x_size', 'standard_price', 'pos_categ_id']


      // let  _data_1 = [];

 const OurAction = AbstractAction.extend({
     // contentTemplate: 'hello_world.ClientAction',
            // setup() {
            //     //  onWillRender(() => {
            //     //   // do something
            //     // });
            //     onMounted(() => {
            //       rpc.query({
            //                     model: model,
            //                     method: 'search_read',
            //                     args: [domain, fields],
            //                 }).then(function (data) {
            //                     console.log(data);
            //                     alert("data loaded")
            //                     _data_1 = data
            //                     });
            //     });
            // },

            // init: function() {
            //      // rpc.query({
            //      //                model: model,
            //      //                method: 'search_read',
            //      //                args: [domain, fields],
            //      //            }).then(function (data) {
            //      //                console.log(data);
            //      //                alert("data loaded")
            //      //            var custom_report = QWeb.render( 'hello_world.ClientAction', {
            //      //                'info': data,
            //      //            });
            //      //            // $( ".o_control_panel" ).addClass( "o_hidden" );
            //      //             $(custom_report).prependTo(self.$el);
            //      //
            //      //    return custom_report
            //      //      });
            // },
             start: async function  () {
                 var self = this;


                 // this._rpc({
                 //
                 //     model: model,
                 //     method: 'search_read',
                 //     args: [domain, fields],
                 // }).then(function (data) {
                 //     self.products = data.length && data;
                 //     // console.log(self.products);
                 //     // alert("data loaded")
                 //     // var custom_report = QWeb.render( 'hello_world.ClientAction', {
                 //     //     'info': data,
                 //     // });
                 //     //      this.$el.html($(QWeb.render( 'hello_world.ClientAction', {
                 //     //     'info': data,
                 //     // })));
                 //     // $( ".o_control_panel" ).addClass( "o_hidden" );
                 //     //  $(custom_report).prependTo(self.$el);
                 //
                 //        console.log("value inside : ",data)
                 //     // return custom_report
                 //     return data
                 // });

                 let response = await this._rpc({

                     model: model,
                     method: 'search_read',
                     args: [domain, fields],
                 })
                 console.log("response : ",arguments)


                 // return $.when(response, this._super.apply(this, arguments));
                 return $.when(response);

                            //   rpc.query({
                            //     model: model,
                            //     method: 'search_read',
                            //     args: [domain, fields],
                            // }).then(function (data) {
                            //     console.log(data);
                            //     alert("data loaded")
                            //     _data_1 = data
                            //     });
                         },
            //  render: function() {
            //     var super_render = this._super;
            //     var self = this;
            //
            //
            // },
          // info: this.state._data_1,
         // template: "hello_world.ClientAction",

              });

    // const OurAction = AbstractAction.extend({      start: function () {          this.$el.html('hello');      }  });
        core.action_registry.add('hello_world.action', OurAction);
        return OurAction;
            });


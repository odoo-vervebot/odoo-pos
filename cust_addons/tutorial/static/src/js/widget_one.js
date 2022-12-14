odoo.define('tutorial.widget_one',
    function (require){
    'use strict'
        console.log("tutorial loaded")
        var AbstractField = require('web.AbstractField');
        var FieldRegistry = require('web.field_registry');

        // create an object with any name
        // don't forget to extend to the web.AbstractField object or its child
        var rpc = require('web.rpc');
        var model = 'product.product';
        var data = "";
        const core = require('web.core');

         var domain = [];
            // Use an empty array to read all the fields of the records
            var fields = ['id','barcode','name'];
            //'product.product', 'search_read', [[['product_variant_count', '=', True]]], {'fields': ['barcode', 'name', 'list_price', 'x_size', 'standard_price', 'pos_categ_id']
            rpc.query({
                model: model,
                method: 'search_read',
                args: [domain, fields],
            }).then(function (data) {





         });

              var WidgetOne = AbstractField.extend({
                    template: 'WidgetOneTemplate', info: data  // fill with the template name that will be rendered by odoo
                });
              // alert("1")
                core.action_registry.add('hello_world.action', WidgetOne);
              // alert("2")
                // register the widget to web.field_registry object
        // so we can use our widget in odoo's view/xml file
        // with the code like below
        // <field name="field_one" widget="widget_one" />
        // the 'widget_one' name is up to you, as long as it's always connected/without spaces'
        FieldRegistry.add('widget_one', WidgetOne);

        // return the widget object
        // so it can be inherited or overridden by another module
        return WidgetOne;
    });
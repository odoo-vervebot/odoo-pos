// odoo.define('hello_world.main', function (require) {  const AbstractAction = require('web.AbstractAction');  console.log(AbstractAction);});
odoo.define('hello_world.main',
    function (require) {  const AbstractAction = require('web.AbstractAction');
    const core = require('web.core');
    var rpc = require('web.rpc');
    var model = 'product.product';

    displayPopup(this)
        {this.DataTable( {dom: 'Qlfrtip'});}






    // Use an empty array to search for all the records
    var domain = [];
    // Use an empty array to read all the fields of the records
    var fields = ['id','barcode','name'];
    //'product.product', 'search_read', [[['product_variant_count', '=', True]]], {'fields': ['barcode', 'name', 'list_price', 'x_size', 'standard_price', 'pos_categ_id']
    rpc.query({
        model: model,
        method: 'search_read',
        args: [domain, fields],
    }).then(function (data) {
        console.log(data);
         const OurAction = AbstractAction.extend({  template: "hello_world.ClientAction",  info: data});
    // const OurAction = AbstractAction.extend({      start: function () {          this.$el.html('hello');      }  });
        core.action_registry.add('hello_world.action', OurAction);});
    });






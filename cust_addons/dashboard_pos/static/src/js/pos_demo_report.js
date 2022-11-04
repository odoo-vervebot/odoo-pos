odoo.define('dashboard_pos.DemoReport', function (require) {
    "use strict";
    
    var AbstractAction = require('web.AbstractAction');
    var ajax = require('web.ajax');
    var core = require('web.core');
    var rpc = require('web.rpc');
    var session = require('web.session');
    var web_client = require('web.web_client');
    var _t = core._t;
    var QWeb = core.qweb;
    
    var PosDemoReport = AbstractAction.extend({
        template: 'PosDemoReport',
        events: {
        },
    
        init: function(parent, context) {
            
            
        },
    
        willStart: function() {
            var self = this;
            return $.when(ajax.loadLibs(this), this._super()).then(function() {
                return self.fetch_data();
            });
        },
    
        start: function() {
            var self = this;
            this.set("title", 'Dashboard');
            return this._super().then(function() {
                self.render_dashboards();
                self.render_graphs();
                self.$el.parent().addClass('oe_background_grey');
            });
        },
    
        fetch_data: function() {
            
            return 10;
        },
    
        render_dashboards: function() {
            var self = this;
                _.each(this.dashboards_templates, function(template) {
                    self.$('.o_pos_demo_report').append(QWeb.render(template, {widget: self}));
                });
        },
           
        
    });
    
    
    core.action_registry.add('pos_demo_report', PosDemoReport);
    
    return PosDemoReport;
    
    });
    
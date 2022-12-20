# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class pos_device_ip(models.Model):
class pos_device_ip_oo(models.Model):
    _inherit = 'pos.config'
    api_url = fields.Char(string='Barcode Device Endpoint',
                               help='Endpoint for device (include protocol (http or https) and port). '
                                    'e.g. http://192.168.1.101:10009')



# class pos_extend_ip(models.Model):
#     _inherit = 'pos.config'
    scale_url = fields.Char(string='Scale Device Endpoint',
                               help='Endpoint for device (include protocol (http or https) and port). '
                                    'e.g. http://192.168.1.101:10009')
    customer_screen_url = fields.Char(string='Scale Device Endpoint', default='http://127.0.0.1:5000',
                               help='Endpoint for device (include protocol (http or https) and port). '
                                    'e.g. http://192.168.1.101:10009')
    
#     _name = 'pos_device_ip.pos_device_ip'
#     _description = 'pos_device_ip.pos_device_ip'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

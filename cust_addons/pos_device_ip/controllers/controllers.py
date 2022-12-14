# -*- coding: utf-8 -*-
# from odoo import http


# class PosDeviceIp(http.Controller):
#     @http.route('/pos_device_ip/pos_device_ip', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_device_ip/pos_device_ip/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_device_ip.listing', {
#             'root': '/pos_device_ip/pos_device_ip',
#             'objects': http.request.env['pos_device_ip.pos_device_ip'].search([]),
#         })

#     @http.route('/pos_device_ip/pos_device_ip/objects/<model("pos_device_ip.pos_device_ip"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_device_ip.object', {
#             'object': obj
#         })

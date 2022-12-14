# -*- coding: utf-8 -*-
# from odoo import http


# class LabelPrint(http.Controller):
#     @http.route('/label_print/label_print', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/label_print/label_print/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('label_print.listing', {
#             'root': '/label_print/label_print',
#             'objects': http.request.env['label_print.label_print'].search([]),
#         })

#     @http.route('/label_print/label_print/objects/<model("label_print.label_print"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('label_print.object', {
#             'object': obj
#         })

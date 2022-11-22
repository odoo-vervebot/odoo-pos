# -*- coding: utf-8 -*-
# from odoo import http


# class OwlLabelPrint(http.Controller):
#     @http.route('/owl_label_print/owl_label_print', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/owl_label_print/owl_label_print/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('owl_label_print.listing', {
#             'root': '/owl_label_print/owl_label_print',
#             'objects': http.request.env['owl_label_print.owl_label_print'].search([]),
#         })

#     @http.route('/owl_label_print/owl_label_print/objects/<model("owl_label_print.owl_label_print"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('owl_label_print.object', {
#             'object': obj
#         })

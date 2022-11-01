# -*- coding: utf-8 -*-
# from odoo import http


# class DirectPrint(http.Controller):
#     @http.route('/direct_print/direct_print', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/direct_print/direct_print/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('direct_print.listing', {
#             'root': '/direct_print/direct_print',
#             'objects': http.request.env['direct_print.direct_print'].search([]),
#         })

#     @http.route('/direct_print/direct_print/objects/<model("direct_print.direct_print"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('direct_print.object', {
#             'object': obj
#         })

# -*- coding: utf-8 -*-
# from odoo import http
#
#
# class PosReports(http.Controller):
#     @http.route('/pos_reports/pos_reports', auth='public')
#     def index(self, **kw):
#         print("controller started")
#         products = http.request.env['product.product'].search([])
#         return http.request.render('pos_reports.nnlisting', {
#             'object': products
#         })
#         pass
#         return "Hello, world"


#     @http.route('/pos_reports/pos_reports/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_reports.listing', {
#             'root': '/pos_reports/pos_reports',
#             'objects': http.request.env['pos_reports.pos_reports'].search([]),
#         })

#     @http.route('/pos_reports/pos_reports/objects/<model("pos_reports.pos_reports"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_reports.object', {
#             'object': obj
#         })

# -*- coding: utf-8 -*-
# from odoo import http


# class Tutorial(http.Controller):
#     @http.route('/tutorial/tutorial', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tutorial/tutorial/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tutorial.listing', {
#             'root': '/tutorial/tutorial',
#             'objects': http.request.env['tutorial.tutorial'].search([]),
#         })

#     @http.route('/tutorial/tutorial/objects/<model("tutorial.tutorial"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tutorial.object', {
#             'object': obj
#         })

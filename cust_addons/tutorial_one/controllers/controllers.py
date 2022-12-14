# -*- coding: utf-8 -*-
# from odoo import http


# class TutorialOne(http.Controller):
#     @http.route('/tutorial_one/tutorial_one', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tutorial_one/tutorial_one/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tutorial_one.listing', {
#             'root': '/tutorial_one/tutorial_one',
#             'objects': http.request.env['tutorial_one.tutorial_one'].search([]),
#         })

#     @http.route('/tutorial_one/tutorial_one/objects/<model("tutorial_one.tutorial_one"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tutorial_one.object', {
#             'object': obj
#         })

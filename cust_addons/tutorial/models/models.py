# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class tutorial(models.Model):
#     _name = 'tutorial.tutorial'
#     _description = 'tutorial.tutorial'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import api, fields, models, exceptions

class Tutorial(models.Model):
    # _inherit = 'product.product'
    _name = 'tutorial.javascript'

    field_one = fields.Integer('Field One', default=1)

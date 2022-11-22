# -*- coding: utf-8 -*-

from odoo import models, fields, api


class label_print(models.Model):
    _inherit = 'product.product'
    _name = 'label_print.label_print'
    _description = 'label_print.label_print'

    description = fields.Text()
    # name = fields.Char()
    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()
    #
    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
    # def get_all_products(self):
    #     orders = self.env['product.product']
    #
    #     if orders:
    #         self.env.cr.execute("""SELECT * FROM product_product
    #             ORDER BY id ASC  """, (tuple(orders.ids),))
    #         categories = self.env.cr.dictfetchall()
    #     return categories
# -*- coding: utf-8 -*-
###################################################################################
#
#    Vervebot.io
#

###################################################################################
import pytz
from odoo import models, fields, api
from datetime import timedelta, datetime, date


class PosDemoReport(models.Model):
    _inherit = 'pos.order'
    # pass



    # @api.model
    # def get_details(self):
    #     company_id = self.env.company.id
    #     cr = self._cr
    #     cr.execute(
    #         """select pos_payment_method.name,sum(amount) from pos_payment inner join pos_payment_method on
    #         pos_payment_method.id=pos_payment.payment_method_id group by pos_payment_method.name ORDER
    #         BY sum(amount) DESC; """)
    #     payment_details = cr.fetchall()
    #     cr.execute(
    #         '''select hr_employee.name,sum(pos_order.amount_paid) as total,count(pos_order.amount_paid) as orders
    #         from pos_order inner join hr_employee on pos_order.user_id = hr_employee.user_id
    #         where pos_order.company_id =''' + str(company_id) + '''GROUP BY hr_employee.name order by total DESC;''')
    #     salesperson = cr.fetchall()
    #     total_sales = []
    #     for rec in salesperson:
    #         rec = list(rec)
    #         sym_id = rec[1]
    #         company = self.env.company
    #         if company.currency_id.position == 'after':
    #             rec[1] = "%s %s" % (sym_id, company.currency_id.symbol)
    #         else:
    #             rec[1] = "%s %s" % (company.currency_id.symbol, sym_id)
    #         rec = tuple(rec)
    #         total_sales.append(rec)
    #     cr.execute(
    #         '''select DISTINCT(product_template.name) as product_name,sum(qty) as total_quantity from
    #    pos_order_line inner join product_product on product_product.id=pos_order_line.product_id inner join
    #    product_template on product_product.product_tmpl_id = product_template.id  where pos_order_line.company_id =''' + str(
    #             company_id) + ''' group by product_template.id ORDER
    #    BY total_quantity DESC Limit 10 ''')
    #     selling_product = cr.fetchall()
    #     sessions = self.env['pos.config'].search([])
    #     sessions_list = []
    #     dict = {
    #         'closing_control': 'Closed',
    #         'opened': 'Opened',
    #         'new_session': 'New Session',
    #         'opening_control': "Opening Control"
    #     }
    #     for session in sessions:
    #         sessions_list.append({
    #             'session': session.name,
    #             'status': dict.get(session.pos_session_state)
    #         })
    #     payments =[]
    #     for rec in payment_details:
    #         rec = list(rec)
    #         sym_id = rec[1]
    #         company = self.env.company
    #         if company.currency_id.position == 'after':
    #             rec[1] = "%s %s" % (sym_id, company.currency_id.symbol)
    #         else:
    #             rec[1] = "%s %s" % (company.currency_id.symbol, sym_id)
    #         rec = tuple(rec)
    #         payments.append(rec)
    #     return {
    #         'payment_details': payments,
    #         'salesperson': total_sales,
    #         'selling_product': sessions_list,
    #     }

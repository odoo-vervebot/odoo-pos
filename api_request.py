
from ast import parse
import xmlrpc.client
from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

    
url = "http://pos.vervebot.io:8069"
db = "postgres3"
username = "info@vervebot.io"
password = "pgadmin"

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
print(common.version())

uid = common.authenticate(db, username, password, {})
# print(uid)

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
# data = (models.execute_kw(db, uid, password, 'product.template', 'check_access_rights', ['read'], {'raise_exception': False}))
# print(data)

# print(models.execute_kw(db, uid, password,
#     'res.partner', 'search',
#     [[['is_company', '=', True], ['customer', '=', True]]]))

# data1 = (models.execute_kw(db, uid, password, 'product.template', 'search', [[['categ_id.name', '=', 'All']]]))
# print(data1)
# print( models.execute_kw(db, uid, password,
#     'res.partner', 'search',
#     [[['is_company', '=', True], ['customer', '=', True]]])
# )
#     {'offset': 10, 'limit': 5})
# )
# print(models.execute_kw(db, uid, password,
#     '', 'search',
#     [[['is_company', '=', True], ['customer', '=', True]]]))

# print(models.execute_kw(
#     db, uid, password, 'res.partner', 'fields_get',
#     [], {'attributes': ['string', 'help', 'type']}))

# print(models.execute_kw(db, uid, password,
#     'product.template', 'read',
#     [data1], {'fields': ['name','barcode']}))

# models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
# data = (models.execute_kw(db, uid, password, 'pos.order', 'check_access_rights', ['read'], {'raise_exception': False}))
# print(data)
# data1 = (models.execute_kw(db, uid, password, 'sale.order', 'search', [[['customer_id.name', '=', 'Undefined']]]))
# data = (models.execute_kw(db, uid, password, 'pos.order', 'search', [[['user_id.name', '=', 'Vervebot']]]))
# print(data)
# print(models.execute_kw(db, uid, password,
#     'pos.order', 'read',
#     [data], {'fields': ['name','date_order']}))


# All product details
'''
data3 = (models.execute_kw(db, uid, password, 'product.product', 'search', [[['available_in_pos', '=', 'All']]],{'offset': 0, 'limit': 1}))
print(data3)

print(models.execute_kw(db, uid, password,
    'product.product', 'read',
    [data3], {'fields': ['id','name','barcode','price']}))
'''

# Single product details
'''
data4 = (models.execute_kw(db, uid, password, 'product.product', 'search', [[['available_in_pos', '=', 'All']]]))
print(data4)

print(models.execute_kw(db, uid, password,
    'product.product', 'read',
    [data4], {'fields': ['id','name','barcode','price']}))
'''
# 
'''
data5 = (models.execute_kw(db, uid, password, 'product.product', 'fields_get',['id','name']))
print(data5)

'''

# selling data in sales module
'''
data6 = (models.execute_kw)(db, uid, password, 'sale.order', 'search', [[['partner_id', '=', 'christopher Phenix']]])
print(models.execute_kw(db, uid, password,
    'sale.order', 'read',
    [data6], {'fields': ['name']}))

'''
# selling data in pos

# data7 = (models.execute_kw(db, uid, password, 'pos.order', 'search', [[['user_id', '=', "Vervebot"]]]))
# print(models.execute_kw(db, uid, password, 'pos.order', 'read', [data7], {'fields': ['name','session_id','date_order','lines', 'payment_ids', 'session_move_id', 'pos_reference']}))

# data8 = (models.execute_kw(db, uid, password, 'pos.order.line', 'search', [[['id', '=', 'ID']]]))
# print(data8)
# print("=============================================================================================================")

# a = (models.execute_kw(db, uid, password, 'pos.order', 'search_read', [[['user_id', '=', 'Vervebot']]],{'fields': ['lines']}))

# print("=============================================================================================================")

# print(models.execute_kw(db, uid, password, 'pos.order.line', 'search',[[['id', '=', '']]], {'fields': ['full_product_name']}))
#create products 
'''
id = (models.execute_kw(db, uid, password, 'product.product', 'create', [{'name': 'testproduct',}]))
print("new recorde fatch",id)

'''

# update product individual 
                                                                          #id        fields
# update = (models.execute_kw(db, uid, password, 'product.product', 'write',[[32449], {'name': 'partner16', 'barcode': 2456355}]))
# print("update record", update)




# emp_id = sock.execute(dbname, uid, pwd, 'hr.employee', 'search', [('barcode','=', '8902579100025')])
# attn_record = {'employee_id': emp_id, 'check_in': '11/10/2020 12:12:12'}
# result = sock.execute(dbname, uid, pwd, 'hr.attendane', 'create', attn_record)

# using barcode product update 

class GetSingle(Resource):
    def get(self):

        parser = reqparse.RequestParser()

        parser.add_argument('barcode', required=True)

        args = parser.parser_args()

        
        product_details = (models.execute(db, uid, password, 'product.product', 'search',[('barcode', '=', args['barcode'])]))

        # product_details = (models.execute(db, uid, password, 'product.product', 'search',[('barcode', '=', '689462000270')]))
       
        # return {'product': args['barcode']}, 200
        return {'product': product_details}, 200
    


# update1 = (models.execute(db, uid, password, 'product.product', 'search',[('barcode', '=', '2456355')]))
# print('successful', update1)


# update = (models.execute_kw(db, uid, password, 'product.product', 'write',[update1, {'name': 'partner17', }]))
# print("update record", update)





# id = (models.execute_kw(db, uid, password, 'product.template', 'fields_get', [{'id': 32449}]))
# ids = models.execute_kw(db, uid, password, 'res.partner', 'read', [32449], {'fields': ['full_product_name']})
# print("new recorde fatch",ids)

# print(models.execute_kw(db, uid, password, 'product.template', 'search_read', [[['product_variant_count', '=', True]]], {'fields': ['barcode', 'name']}))

api.add_resource(GetSingle,'/GetSingle')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5010)

# import xmlrpc.client


# url = 'http://pos.vervebot.io:8069'

# db = 'postgres3'

# username= 'info@vervebot.io'

# password= 'pgadmin'

# conn = xmlrpc.client.ServerProxy('{0}/xmlrpc/common?db={1}'.format(url,db))


# uid = conn.login(db,username,password)
# print(uid)


# models = xmlrpc.client.ServerProxy('{0}/xmlrpc/object?db={1}'.format(url,db))

# print(models)

# # ids = [ your searched id(s) ]

# x=models.execute_kw(db, uid, password, 'sale.order','read',id)
# print(x)

 

# a = models.exec_workflow(db,uid,password,'student.info.workflow','check',ids[0])

 

# x=models.execute_kw(db, uid, password, 'student.info.workflow','read',ids)


from ast import parse
import xmlrpc.client
from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

url = "http://pos.vervebot.io:8069"
db = "postgres3"
username = "vervebot@gmail.com"
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

data7 = (models.execute_kw(db, uid, password, 'pos.order', 'search_read', [[['user_id', '=', "Vervebot"]]]))
print(models.execute_kw(db, uid, password, 'pos.order', 'read', [data7], {'fields': ['name','session_id','date_order','lines', 'payment_ids', 'session_move_id', 'pos_reference']}))

data8 = (models.execute_kw(db, uid, password, 'pos.order.line', 'search', [[['id', '=', 'ID']]]))
print(data8)


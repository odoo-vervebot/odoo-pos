import xmlrpc.client

url = "http://44.204.149.152:8069"
db = "postgre3"
username = "odoo17"
password = "admin"

import xmlrpc.client

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
version = common.version()
print("details...", version)
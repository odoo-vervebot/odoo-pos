# a = [{'name': 'Undefined', 'suppliers': '', 'product_name': 'test', 'qty': 1.0, 'sale_amount': 1.0, 'tax_amount': 0.0, 'cost': 1.0, 'sale': 1.0, 'total_cost': 1.0, 'gross_profit': 0.0, 'date': '02/11/2022'}, {'name': 'Undefined', 'suppliers': '', 'product_name': 'test add from pos screen', 'qty': 1.0, 'sale_amount': 10.0, 'tax_amount': 0.0, 'cost': 0.0, 'sale': 10.0, 'total_cost': 0.0, 'gross_profit': 10.0, 'date': '02/11/2022'}, {'name': 'Undefined', 'suppliers': '', 'product_name': 'test', 'qty': 5.0, 'sale_amount': 5.0, 'tax_amount': 0.0, 'cost': 1.0, 'sale': 1.0, 'total_cost': 5.0, 'gross_profit': 0.0, 'date': '21/10/2022'}, {'name': 'Undefined', 'suppliers': '', 'product_name': 'test', 'qty': 6.0, 'sale_amount': 6.0, 'tax_amount': 0.0, 'cost': 1.0, 'sale': 1.0, 'total_cost': 6.0, 'gross_profit': 0.0, 'date': '28/10/2022'}]

# print(a)

# newlist = sorted(a, key=lambda d: d['qty']) 
from operator import itemgetter

my_list = [{'name':'Homer', 'age':39}, {'name':'Bart', 'age':10}]
newlist = sorted(my_list, key=itemgetter('age') , reverse=True) 
print(newlist)
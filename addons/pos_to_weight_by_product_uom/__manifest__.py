# Copyright 2017, Grap
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
#{
    #"name": "Pos to weight by product uom",
    #"summary": "Make 'To Weight' default value"
    #" depending on product UoM settings",
    #"version": "12.0.1.0.0",
    #"website": "https://github.com/OCA/pos",
    #"author": "GRAP, Odoo Community Association (OCA)",
    #"development_status": "Beta",
    #"license": "AGPL-3",
    #"installable": True,
    #"depends": [
        #"point_of_sale",
    #],
    #"data": [
        #'views/view_uom_uom.xml',
        #'views/view_uom_category.xml',
    #],
    #'demo': [
        #'demo/res_groups.xml',
        #'demo/uom_category.xml',
        #'demo/uom_uom.xml',
    #]
#}

{
    'name': "Pos to weight by product uom",
    'version': '12.0.1.0.0',
    "author": "GRAP, Odoo Community Association (OCA) " ,
    "development_status": "Beta" ,
    'sequence': -100,
    'summary': '',
    'description': "",
    'depends': [
        "point_of_sale",
    ],
    'data': [
        'views/view_uom_uom.xml',
        'views/view_uom_category.xml',
        
    ],
    'demo': [
        'demo/res_groups.xml',
        'demo/uom_category.xml',
        'demo/uom_uom.xml',

    ],
    
    'installable': True,
    'application': True,
    "website": "https://github.com/OCA/pos",
    'assets': {
        
    },
    'license': 'AGPL-3',
}
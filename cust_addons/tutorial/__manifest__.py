# -*- coding: utf-8 -*-
{
    'name': "tutorial",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',"web", 'product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        # 'views/assets.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
            'web.assets_backend': [
                     'tutorial/static/src/xml/widget_one.xml',
                     'tutorial/static/src/js/widget_one.js',
            ]
        },
    # "qweb": [
    #         "static/src/xml/widget_one.xml"
    #         "static/src/js/widget_one.js"
    #     ],
    "license": 'LGPL-3',
    "installable": True
}

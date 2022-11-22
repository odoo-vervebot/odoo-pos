# -*- coding: utf-8 -*-
{
    'name': "pos_reports",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Vervebot",
    'website': "http://www.vervebot.io",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','point_of_sale'],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    # 'qweb': ['pos_reports/static/src/xml/hello_world.xml'],
    'assets': {
        'web.assets_backend': [
             'pos_reports/static/src/js/hello_world.js',
             'https://cdn.datatables.net/1.13.1/js/jquery.dataTables.min.js',
             'https://cdn.datatables.net/searchbuilder/1.4.0/js/dataTables.searchBuilder.min.js',
             'https://cdn.datatables.net/datetime/1.2.0/js/dataTables.dateTime.min.js',
             'pos_reports/static/src/js/custom.js',
             'https://cdn.datatables.net/1.13.1/css/jquery.dataTables.min.css',
             'https://cdn.datatables.net/searchbuilder/1.4.0/css/searchBuilder.dataTables.min.css',
             'https://cdn.datatables.net/datetime/1.2.0/css/dataTables.dateTime.min.css',
             'pos_reports/static/src/css/hello_world.css',
         ],
        'web.assets_qweb': [
            'pos_reports/static/src/xml/hello_world.xml',
        ],
     }
}

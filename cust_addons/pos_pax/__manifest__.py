# Clover Rest API payment. See LICENSE_PROFESSIONAL file for full copyright and licensing details.

{
    'name': 'Clover Payment',
    'author': 'vervebot <info@vervebot.io>',
    'version': '15.0.1.0.0',
    'category': 'Point of Sale',
    'sequence': 6,
    'summary': 'Clover payment for Point Of Sale',
    'description': """
Allow Clover Rest API payments
==============================

This module allows customers to pay for their orders with clover device. 
The transactions are processed on the clover device (no credit credit card 
information through Odoo itself). 

Depending on Device and processor support, this integration can handle:

* Magnetic swiped cards
* EMV chip cards
* Contactless (including Apple Pay, Samsung Pay, Google Pay)

    """,
    'depends': [
        'pos_sale',
        
    ],
    'website': 'https://vervebot.io',
    'data': [
        'views/pos_config_setting_views.xml',
        'views/pos_pax_views.xml',
    ],
    'demo': [
    ],
    'assets': {
        'web.assets_qweb': [
            'pos_pax/static/src/xml/OrderReceipt.xml',
            'pos_pax/static/src/xml/PAXPaymentTransactionPopup.xml',
            'pos_pax/static/src/xml/PAXPaymentScreenPaymentLines.xml',
        ],
        'point_of_sale.assets': [
            'pos_pax/static/src/js/jquery_base64.js',
            'pos_pax/static/src/js/pax_device.js',
            'pos_pax/static/src/js/pos_pax.js',
            'pos_pax/static/src/js/PAXPaymentTransactionPopup.js',
            'pos_pax/static/src/js/PAXPaymentScreen.js',
            'pos_pax/static/src/js/PAXPaymentScreenPaymentLines.js',
            'pos_pax/static/src/css/pos_pax.css',
        ],
    },
    'installable': True,
    'auto_install': False,
    'license': 'OPL-1',
}

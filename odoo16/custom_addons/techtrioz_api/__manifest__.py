# -*- coding: utf-8 -*-
#########################################
#     Developed by: TechTrioz
#########################################

{
    'name': "Techtrioz API",

    'summary': """APIs for RFID.""",

    'description': """
        This module includes the following features:
            - Customized Login API endpoint
            - 
    """,

    'author': "Techtrioz Solutions",
    'website': "https://techtrioz.com/",
    'license': 'LGPL-3',

    'category': 'Technical',
    'version': '16.0.1.0.2',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'product',
        'stock',
        'stock_picking_batch',
        'sale',
        'purchase',
        'mrp',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/ir_rule.xml',
        'data/data.xml',
        'data/ir_sequence.xml',
        'data/stock_warehouse_cron.xml',
        'views/res_users.xml',
        'views/stock_picking.xml',
        'views/res_config_settings_view.xml',
        'views/stock_location_view.xml',
        'views/product_template_views.xml'
    ],
    "post_init_hook": "_post_init_pick_hook",
    'application': True,
    'sequence': 1,
}

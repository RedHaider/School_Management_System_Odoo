# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Testing Module',
    'version': '1.0.0',
    'category': 'Testing',
    'author': 'Haider',
    'sequence': -100,
    'summary': 'Testing Module',
    'description': """This is a testing module where i will implement almost everthing""",
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        # 'security/security.xml',
        'views/menu_views.xml',
        'views/testing_one_view.xml',
        'views/testing_two_view.xml',
    ],

    'demo': [],
    'application': True,
    'auto_install': False,
    'assets': {},
    'license': 'GPL-3',
}

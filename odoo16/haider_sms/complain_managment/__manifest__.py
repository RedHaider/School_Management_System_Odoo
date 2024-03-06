# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Complain Management',
    'version': '1.0.0',
    'category': 'Complain',
    'author': 'Israt Jahan Katha Moni',
    'sequence': -100,
    'summary': 'Complain management system',
    'description': """Complain Management system""",
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/menu_views.xml',
        'views/employee_complain_views.xml',
    ],

    'demo': [],
    'application': True,
    'auto_install': False,
    'assets': {},
    'license': 'GPL-3',
}

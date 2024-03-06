# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Hospital Management',
    'version': '1.0.0',
    'category': 'Hospital',
    'author':'Hospital',
    'sequence':-100,
    'summary': 'Hospital management system',
    'description': """Hospital Management system""",
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
             'security/security.xml',
             'views/menu.xml',
             'views/patient_view.xml',
             'views/doctor_view.xml',
             'views/ward_view.xml',
             'views/sales_quotation.xml',
             'data/server_cron.xml',
             'views/patient_transient.xml',
             'data/sequence.xml'],
    'demo': [],
    'application':True,
    'auto_install': False,
    'assets': {},
    'license': 'GPL-3',
}

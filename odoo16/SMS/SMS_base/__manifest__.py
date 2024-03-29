# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'School Management System',
    'version': '1.0.0',
    'category': 'education',
    'author': 'techtrios',
    'sequence': -100,
    'summary': 'Educational Module',
    'description': """This is a educational Modules can be used by school""",
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        # 'security/security.xml',
        'views/menu_views.xml',
        'views/school_student_views.xml',
        'views/school_teacher_views.xml',
        'views/school_parent_views.xml',
        #configure xmls
        'views/school_class_views.xml',
        'views/school_room_views.xml',
        'views/school_section_views.xml',
        'views/school_subject_views.xml',
    ],

    'demo': [],
    'application': True,
    'auto_install': False,
    'assets': {},
    'license': 'GPL-3',
}

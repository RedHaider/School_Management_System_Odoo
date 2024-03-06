#########################################
#     Developed by: TechTrioz_Haider
#########################################

{
    'name': 'School Management System',
    'version': '16.0.1.0',
    'sequence': 3,
    'summary': 'School management system deals with the demands of school',
    'description': '''
        TechTrioZ SMS Description.
    ''',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/menu_view.xml',
        'views/school_admin_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'AGPL-3',  # Add your desired license type
}

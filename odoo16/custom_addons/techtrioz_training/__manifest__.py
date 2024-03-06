{
    'name': 'Techtrioz Training',
    'version': '1.0.0',
    'sequence': -100,
    'summary': 'Techtrioz Training',
    'description': 'Techtrioz Training',
    'author': 'Techtrioz',  # Replace 'Your Name' with your name or your organization's name.
    'license': 'GPL-3',  # Specify the correct license for your module.
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/trainee_master.xml',
        'views/designation_master_view.xml',
        'views/trainee_location_master_view.xml',
        'views/trainer_master_view.xml',
        'views/training_subjects_view.xml',
        'views/training_topics_view.xml',
        'views/training_stages_view.xml',
        'views/employee_master.xml',
        'views/trainee_transient.xml',
    ],
    'depends': ['base'],
    'installable': True,
    'application': True,
    'auto_install': False,
}

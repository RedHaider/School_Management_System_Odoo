#########################################
#     Developed by: TechTrioz
#########################################


{
    'name': 'Techtrioz Custom Modifications',
    'version': '16.0.1.0',
    'sequence': 1,
    'summary': 'Techtrionz Custom Modifications Summery',
    'description': '''
       Techtrionz Custom Modifications Description.
    ''',
    'depends': ['base','sale_management','purchase','sale'],
    'data': [ 
        'views/custom_pick_note_view.xml',
        'views/custom_sale_note_view.xml',
        'views/custom_purchase_note_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
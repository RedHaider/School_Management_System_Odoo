#########################################
#     Developed by: TechTrioz
#########################################


{
    'name': 'Techtrioz Sale Replica',
    'version': '1.0.0',
    'sequence': -100,
    'summary': 'Techtrioz Sale Replica',
    'description': 'Techtrioz Sale Replica',
    'author': 'Techtrioz',  # Replace 'Your Name' with your name or your organization's name.
    'license': 'GPL-3',  # Specify the correct license for your module.
    'description': '''
        Techtrioz Sale Replica.
    ''',
    'depends': ['base','product','account','sale'],
    'data': [
             'security/ir.model.access.csv',
             'data/sequence.xml',
             'views/menu.xml',
             'views/custom_sale_order_replica_view.xml',
             'views/custom_sale_order_line_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False

}
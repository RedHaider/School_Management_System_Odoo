#########################################
#     Developed by: TechTrioz
#     website: techtrioz.com
#########################################

{
    'name': 'Hr Custom',
    'version': '16.0.1.0',
    'sequence': 1,
    'author': 'TechTrioz',
    'license': 'AGPL-3',
    'summary': 'TechTrioZ Hr Custom',
    'description': '''
        TechTrioZ Purchase Hr Description.
    ''',
    'depends': ['base','crm','sale_management'],
    'data': [
      'views/product_template_view.xml'

    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
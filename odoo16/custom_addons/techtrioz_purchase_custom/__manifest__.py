#########################################
#     Developed by: TechTrioz
#     website: techtrioz.com
#########################################

{
    'name': 'TechTrioz Purchase Custom',
    'version': '16.0.1.0',
    'sequence': 1,
    'author': 'TechTrioz',
    'license': 'AGPL-3',
    'summary': 'TechTrioZ Purchase Custom',
    'description': '''
        TechTrioZ Purchase Custom Description.
    ''',
    'depends': ['base','purchase','product','crm','sale_management'],
    'data': [
        'views/purchase_order_views.xml',
        'views/my_product_template_view.xml',
        'views/sales_productvariant.xml',
        # 'views/crm_lead_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
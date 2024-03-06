#########################################
#     Developed by: TechTrioz
#     website: techtrioz.com
#########################################

{
    'name': 'CRM Custom',
    'version': '16.0.1.0',
    'sequence': 1,
    'author': 'TechTrioz',
    'license': 'AGPL-3',
    'summary': 'TechTrioZ CRM Custom',
    'description': '''
        TechTrioZ Purchase CRM Description.
    ''',
    'depends': ['base','crm','sale_management'],
    'data': [
      'data/crm_template_data.xml',
      'views/crm_lead_custom_view.xml',
      'views/crm_lead_page_view.xml',
      'views/product_image_view.xml',
      'views/product_template_view.xml'

    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
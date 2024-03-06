#########################################
#     Developed by: TechTrioz
#     website: techtrioz.com
#########################################

from odoo import models, fields, api

class ProductTemplet(models.Model):
    _inherit = 'product.template'
    _description = 'Product Template'

    product_brand = fields.Char(string='Product Brand')
    dealer_name = fields.Many2one('res.partner', string='Dealer Name') 


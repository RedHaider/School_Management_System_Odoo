#########################################
#     Developed by: TechTrioz
#     website: techtrioz.com
#########################################

from odoo import models, fields

#inheritance operation
class MyProductTemplate(models.Model):
    _inherit = 'product.template'

#the fields to send. 
    product_brand = fields.Char(string="Product Brand")
    dealer_name = fields.Many2one('res.partner', string="Dealer Name")

#########################################
#     Developed by: TechTrioz
#     website: techtrioz.com
#########################################

from odoo import models, fields, api


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    product_id = fields.Many2one('product.template', string="Product")
    image = fields.Binary(string='Image')
    related_image = fields.Binary(string='Uploaded Image', related='image',readonly=True)

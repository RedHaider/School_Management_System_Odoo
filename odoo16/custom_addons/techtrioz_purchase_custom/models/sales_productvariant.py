#########################################
#     Developed by: TechTrioz
#     website: techtrioz.com
#########################################

from odoo import models, fields


class PurchaseOrderLine(models.Model):
    _inherit = 'product.product'

    product_image = fields.Binary(string='Product Image')
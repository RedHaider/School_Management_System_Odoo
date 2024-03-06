#########################################
#     Developed by: TechTrioz
#     website: techtrioz.com
#########################################

from odoo import models, fields, api

class ProductImage(models.Model):
    _inherit = 'product.product'
    _description = 'Product Image'

    product_image = fields.Binary(string='Design')
    combined_info = fields.Char(string='Product Info', compute='_compute_combined_info')
    file = fields.Binary(string='Upload file', attachment=True)
    file_name = fields.Char(string='File Name',help="This is file upload option")
    attachment_ids = fields.Many2many('ir.attachment', string="Attachments",attachment=True,
                                  help="any attachments")
    def _compute_combined_info(self):
        for product in self:
            product.combined_info = f"{product.default_code} - {product.name}"

    

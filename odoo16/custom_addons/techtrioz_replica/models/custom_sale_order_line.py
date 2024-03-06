#########################################
#     Developed by: TechTrioz
#########################################


from odoo import models, fields, api,_
from odoo.exceptions import ValidationError

class CustomSaleOrderLine(models.Model):
    _name = 'custom.sale.order.line'
    _description = 'Custom Sale Order Line'

    product_template_id = fields.Many2one('product.template', string='Product', required=True)
    description = fields.Text(string='Description')
    product_uom_qty = fields.Float(string='Quantity', digits='Product Unit of Measure')
    product_uom = fields.Many2one('uom.uom', string='UOM')
    price_unit = fields.Monetary(string='Unit Price', currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Currency')

    order_id = fields.Many2one('custom.sale.order', string='Order')
   
    tax_id = fields.Many2many('account.tax', string='Taxes')
    price_subtotal = fields.Monetary(string='Subtotal', compute='_compute_subtotal', store=True)

    @api.depends('product_uom_qty', 'price_unit')
    def _compute_subtotal(self):
       for line in self:
        line.price_subtotal = line.product_uom_qty * line.price_unit
    
    
    @api.onchange('product_template_id')
    def onchange_product_template_id(self):
         if self.product_template_id:
            self.price_unit = self.product_template_id.list_price
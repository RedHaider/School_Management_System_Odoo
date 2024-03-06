#########################################
#     Developed by: TechTrioz
#########################################


from odoo import models, fields, api,_
from odoo.exceptions import ValidationError

class StockRule(models.Model):
    _inherit = 'stock.rule'
    
    @api.depends( 'pick_note_line','sale_note_line')
    def _get_stock_move_values(self, product_id, product_qty, product_uom, location_id, name, origin, company_id, values):
        move_values = super()._get_stock_move_values(product_id, product_qty, product_uom, location_id, name, origin, company_id, values)
       
        move_values.update({
            'pick_note_line': values.get('sale_note_line'),
        })
        return move_values
# purchase_note/models/purchase_note.py

from odoo import models, fields, api,_
from odoo.exceptions import ValidationError

class PurchaseNote(models.Model):
    _inherit = 'purchase.order'
    _description = 'Purchase Note'
    
    purchase_note = fields.Char(string='Purchase Note')
    
    @api.depends('picking_ids', 'purchase_note')
    def button_confirm(self):
        res = super(PurchaseNote, self).button_confirm()

        for picking in self.picking_ids:
            picking.write({'pick_note': self.purchase_note})

        return res  
    
class PurchaseNoteLine(models.Model):
    _inherit = 'purchase.order.line'
    _description = 'Purchase line note'

    purchase_note_line = fields.Char(string='Purchase Note')
    
    @api.depends( 'pick_note_line','purchase_note_line')
    def _prepare_stock_move_vals(self, picking, price_unit, product_uom_qty, product_uom):
        values = super(PurchaseNoteLine, self)._prepare_stock_move_vals(picking, price_unit, product_uom_qty, product_uom)
        values.update({
            'pick_note_line': self.purchase_note_line ,
        })
        return values
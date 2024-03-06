#########################################
#     Developed by: TechTrioz
#########################################


from odoo import models, fields, api,_
from odoo.exceptions import ValidationError


class SaleNote(models.Model):
    _inherit = 'sale.order'
    _description = 'Sale Note'

    sale_note = fields.Char(string='Sale Note')
    

    @api.depends('picking_ids', 'sale_note')
    def action_confirm(self):
        res = super(SaleNote, self).action_confirm()

        for picking in self.picking_ids:
            picking.write({'pick_note': self.sale_note})

        return res
    
class SaleNoteLine(models.Model):
    _inherit = 'sale.order.line'
    _description = 'Sale order line note'

    sale_note_line = fields.Char(string='Line Note')

    @api.depends('picking_ids', 'sale_note_line')
    def _prepare_procurement_values(self, group_id=False):
        self.ensure_one()
        values = super(SaleNoteLine, self)._prepare_procurement_values(group_id=group_id)
        values.update({
            'sale_note_line': self.sale_note_line,
        })

        return values

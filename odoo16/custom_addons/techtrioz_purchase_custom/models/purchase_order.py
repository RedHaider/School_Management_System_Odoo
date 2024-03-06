#########################################
#     Developed by: TechTrioz
#     website: techtrioz.com
#########################################

from odoo import models, fields, api


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    remarks = fields.Char(string="Remarks")


    
    def my_button_action(self):
        self.ensure_one()
        action = {
            'name': 'Stock Quant Tree Editable',  # Set a name for the action
            'type': 'ir.actions.act_window',
            'res_model': 'stock.quant',
            'view_mode': 'form',
            'view_id': self.env.ref('stock.view_stock_quant_tree_inventory_editable').id,
            'target': 'new',
            'domain': [('id', '=', self.product_id.id)]
        }
        return action
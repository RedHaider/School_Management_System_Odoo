#########################################
#     Developed by: TechTrioz
#########################################


from odoo import models, fields, api,_
from odoo.exceptions import ValidationError


class PickNote(models.Model):
    _inherit = 'stock.picking'
    _description = 'Pick Note'

    pick_note = fields.Char(string='Pick Note')

class PickNoteLine(models.Model):
    _inherit = 'stock.move'
    _description = 'Stock Moved Line'

    pick_note_line = fields.Char(string='Line Note')

    
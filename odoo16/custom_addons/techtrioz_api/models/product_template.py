#########################################
#     Developed by: TechTrioz
#########################################


from odoo import models, fields, api,_
from odoo.exceptions import ValidationError


class SaleNote(models.Model):
    ''' Inherited to pass the rfid data'''
    _inherit = 'product.template'


    rfid = fields.Char(string='RFID')

   
    
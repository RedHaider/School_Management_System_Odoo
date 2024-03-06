from odoo  import models, fields, api

class Designation(models.Model):
    _name = 'techtrioz.trainee.designation'
    _description = 'Designation/Role Master'

    name = fields.Char(string= 'Name', required= True)
    sequence = fields.Char(string='Sequence', default=lambda self: self.env['ir.sequence'].next_by_code('techtrioz.trainee.designation'))

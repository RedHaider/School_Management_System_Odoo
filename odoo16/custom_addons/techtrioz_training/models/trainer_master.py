from odoo import models, fields, api

class TrainerMaster(models.Model):
    _name = 'techtrioz.trainer'
    _description = 'Trainder Master'

    name = fields.Char(string='Name', compute='_compute_name', store=True, readonly=True )
    first_name= fields.Char(string='Fist Name')
    last_name =fields.Char(string='Last Name')
    profile_image = fields.Image(string='Profile Image')

    @api.depends('first_name','last_name')
    def _compute_name(self):
        for record in  self:
            record.name = f"{record.first_name} {record.last_name}"
    
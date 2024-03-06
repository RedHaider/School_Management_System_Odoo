from odoo import models, fields

class techtriozLocation(models.Model):
    _name = 'techtrioz.location'
    _description = 'Trainee Location Master'
    _rec_name = 'location_name'

    location_name = fields.Char(string='Location Name', required=True)
    street1 = fields.Char(string='Street 1')
    street2 = fields.Char(string='Street 2')
    city = fields.Char(string='City')
    state_id = fields.Many2one('res.country.state', string='State')
    country_id = fields.Many2one('res.country', string='Country')

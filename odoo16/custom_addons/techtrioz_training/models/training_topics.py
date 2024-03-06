from odoo import models, fields
class TrainingTopics(models.Model):
    _name = 'techtrioz.training.topic'
    _description = 'Training Topics'

    name = fields.Char(string='Name', required=True)
    subject = fields.Many2one('techtrioz.training.subject', string='Subject')

    
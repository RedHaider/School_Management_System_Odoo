from odoo import models, fields

class TrainingSubjects(models.Model):
    _name = 'techtrioz.training.subject'
    _description = 'Training Subjects'

    name = fields.Char(string='Name', required= True)
    description =fields.Html(string='Description')
    topics= fields.One2many('techtrioz.training.topic', 'subject',string='Topics')
    trainers = fields.Many2many('techtrioz.trainer' ,string='Trainers')
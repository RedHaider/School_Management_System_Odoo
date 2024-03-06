from odoo import models, fields

class TrainingStages(models.Model):
    _name = 'techtrioz.training.stages'
    _description = 'Training Stages'

    name = fields.Char(string='Name', required=True, help='Ex: New(draft), Pending Confirm(draft), Trainee Confirmed(progress), Training Started(progress), Training Completed(progress), Employed(Done)')
    available_on_batch = fields.Boolean(string='Available on Batch')
    available_on_training_record = fields.Boolean(string='Available on Training Record')
    state = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('progress', 'Progress'),
            ('done', 'Done')
        ],
        string='Status', required=True, default='draft'
    )
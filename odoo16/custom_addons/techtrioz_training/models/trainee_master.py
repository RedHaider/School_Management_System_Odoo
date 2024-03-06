from odoo import models, fields, api, _
import logging
_logger = logging.getLogger(__name__)

class TraineeMaster(models.Model):
    _name = 'techtrioz.trainee.master'
    _description = 'Trainee Master'


    name = fields.Char(string='Name', compute='_compute_name' , store=True, readonly=True)
    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name')
    trainee_id = fields.Char(
        string='Trainee ID',
        copy=False,
        readonly=True,
        index=True,
        default=lambda self: self._generate_trainee_id() or ''
    )
    emp_code = fields.Char(string='EMP Code')
    personal_email_id = fields.Char(string='Personal Email ID' )
    linked_profile_url= fields.Char(string='Linked Profile URL')
    gender = fields.Selection(selection=[('male','Male'),('female','Female')], string= 'Gender', required=True, default='male')
    dob = fields.Date(string='DOB')
    date_of_joining = fields.Date(string='Date of Joining')
    locaton_id = fields.Many2one('techtrioz.location', string='Location', required=False)
    designation_id = fields.Many2one('techtrioz.trainee.designation', string='Designation')
    profile_image= fields.Binary(string='Profile Image')
    status = fields.Selection(selection=[
        ('new','New'),
        ('employed','Employed'),
    ],string='Status', default='new')

    #employee_id = fields.Many2one('hr.employee', string='Employee')

    def action_done(self):
        action = {
            'name': 'Transient',  # Set a name for the action
            'type': 'ir.actions.act_window',
            'res_model': 'trainee.transient',
            'view_mode': 'form,tree',
            'view_id': False,
            'target': 'new',
            'context':{'default_trainee_id':self.id}
        }
        return action

    # def action_done(self):
    #     if self.status == 'new':
    #         self.status = 'employed'

    #         # Create a record in employee.master
    #         self.env['techtrioz.employee.master'].create({
    #             'name': self.name,
    #             'first_name': self.name,
    #             'last_name': self.name,
    #             'emp_code': self.emp_code,
    #             'personal_email_id': self.personal_email_id,
    #             'linked_profile_url': self.linked_profile_url,
    #             'gender': self.gender,
    #             'dob': self.dob,
    #             'date_of_joining': self.date_of_joining,
    #             'locaton_id': self.locaton_id.id,
    #             'designation_id': self.designation_id.id,
    #             'profile_image': self.profile_image,
    #             # Add more fields as needed
    #         })

            
    # def _cron_patient(self):
    #     for rec in self:
    #         if rec.state == 'new':
    #             rec.state = 'employed'
    #         else:
    #             rec.state = 'new'

    @api.depends('first_name','last_name')
    def _compute_name(self):
        for record in  self:
            record.name = f"{record.first_name} {record.last_name}"
    
    # @api.depends('first_name','last_name')
    # def _compute_trainee_id(self):
    #     for record in self:
    #         record.trainee.id = f"{record.first_name[:3]}{record.last_name[:3]}"

    _sql_constraints = [
        ('unique_trainee_id', 'unique(trainee_id)', 'Trainee ID must be unique.')
    ]

    @api.model
    def _generate_trainee_id(self):
        try:
            sequence_value = self.env['ir.sequence'].next_by_code('techtrioz.trainee')
            if sequence_value:
                _logger.info(f"Generated Trainee ID: {sequence_value}")
                return sequence_value
            else:
                _logger.warning("Failed to generate Trainee ID: Sequence returned False.")
                return ''
        except Exception as e:
            _logger.error(f"Error generating Trainee ID: {e}")
            return ''
        
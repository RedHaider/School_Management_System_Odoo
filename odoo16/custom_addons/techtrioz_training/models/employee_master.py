from odoo import models, fields, api, _
import logging
_logger = logging.getLogger(__name__)

class TraineeMaster(models.Model):
    _name = 'techtrioz.employee.master'
    _description = 'Trainee Master'


    name = fields.Char(string='Name', compute='_compute_name' , store=True, readonly=True)
    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name')
    emp_code = fields.Char(string='EMP Code')
    personal_email_id = fields.Char(string='Personal Email ID' )
    linked_profile_url= fields.Char(string='Linked Profile URL')
    gender = fields.Selection(selection=[('male','Male'),('female','Female')], string= 'Gender', required=True, default='male')
    dob = fields.Date(string='DOB')
    date_of_joining = fields.Date(string='Date of Joining')
    locaton_id = fields.Many2one('techtrioz.location', string='Location', required=False)
    designation_id = fields.Many2one('techtrioz.trainee.designation', string='Designation')
    profile_image= fields.Binary(string='Profile Image')
    employee_id = fields.Char(string='Employee')
    
    
    #employee_id = fields.Many2one('hr.employee', string='Employee')

    @api.depends('first_name','last_name')
    def _compute_name(self):
        for record in  self:
            record.name = f"{record.first_name} {record.last_name}"
    

        
# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError



class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient"

    f_name = fields.Char(string='First Name')
    l_name = fields.Char(string='Last Name')
    fullname = fields.Char(string='Full Name', compute='_compute_full_name', store=True, readonly=False)
    age = fields.Integer(string="Age")
    code = fields.Integer(string="Code")
    gender = fields.Selection([('male','Male'),('female','Female'),('others','Others')], string="Gender")
    doctor = fields.Many2one('hospital.doctor',string='Doctor')
    ward =fields.Many2one('hospital.ward',string='Ward')
    state=fields.Selection(
        selection=[
            ('new','New'),
            ('done','Done'),
        ], string='State',default='new' )
    user_id = fields.Many2one('res.users', string="Related Users", default=lambda self: self.env.user)
    
    trainee_id = fields.Char(
        string='Trainee ID',
        copy=False,
        readonly=True,
        index=True,
        default=lambda self: _('New')
    )
    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('trainee_id', ('New')) == ('New'):
                vals['trainee_id'] = self.env['ir.sequence'].next_by_code('trainee_id.sequence') or _('New')

        return super().create(vals_list)
    
    def action_done(self):
        print("################")
        if self.state == 'new':
            self.state = 'done'

    def action_ward(self):
        self.ensure_one()
        action = {
            'name': 'Appointment',  # Set a name for the action
            'type': 'ir.actions.act_window',
            'res_model': 'hospital.patient.appointment',
            'view_mode': 'tree,form',
            'view_id': False,
            'target': 'new',
        }
        return action

    def _cron_patient(self):
        print("Urgent CheckUp needed")
        for rec in self:
            if rec.state == 'new':
                rec.state = 'done'
            else:
                rec.state = 'new'


    @api.depends('f_name','l_name')
    def _compute_full_name(self):
        for record in self:
            if record.f_name and record.l_name:
                record.fullname = f'{record.f_name} {record.l_name}'
            else:
                record.fullname= record.f_name or record.l_name
    
    _sql_constraints = [
        ('unique_code','UNIQUE(code)','Code must be unqiue'),
    ]

    @api.constrains('code')
    def _check_code_length(self):
        for record in self:
            if record.code:
                code_str = str(record.code)
                if len(code_str) != 5:
                    raise ValidationError("Code must be exactly 5 charactera long.")

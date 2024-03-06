from odoo import models, fields, api

class TransientAppointment(models.TransientModel):
    _name = 'hospital.patient.appointment'
    _description= 'Patient Appointment'

    f_name = fields.Char(string='First Name')
    l_name = fields.Char(string='Last Name')
    fullname = fields.Char(string='Full Name', compute='_compute_full_name', store=True, readonly=False)
    age = fields.Integer(string="Age")
    gender = fields.Selection([('male','Male'),('female','Female'),('others','Others')], string="Gender")
    doctor = fields.Many2one('hospital.doctor', string='Doctor')
    date = fields.Date(string='Date', required=True)

    @api.depends('f_name', 'l_name')
    def _compute_full_name(self):
        for record in self:
            record.fullname = f"{record.f_name} {record.l_name}"
    
    def save_transient(self):
        history_model = self.env['hospital.patient']
        for record in self:
            vals = {
                'f_name': record.f_name,
                'l_name': record.l_name,
                'age': record.age,
                'gender': record.gender,
                'doctor': record.doctor.id,
            }
            history_model.create(vals)
        

        
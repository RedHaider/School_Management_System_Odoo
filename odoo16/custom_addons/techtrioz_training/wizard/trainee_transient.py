from odoo import models, fields, api

class TraineeTransient(models.TransientModel):
    _name = 'trainee.transient'
    _description= 'Trainee Transient'

    employee_id = fields.Char(string='Employee')
    trainee_id = fields.Many2one('techtrioz.trainee.master', string='Trainee ID')

    # @api.depends('f_name', 'l_name')
    # def _compute_full_name(self):
    #     for record in self:
    #         record.fullname = f"{record.f_name} {record.l_name}"
    
    # def save_transient(self):
    #     history_model = self.env['hospital.patient']
    #     for record in self:
    #         vals = {
    #             'f_name': record.f_name,
    #             'l_name': record.l_name,
    #             'age': record.age,
    #             'gender': record.gender,
    #             'doctor': record.doctor.id,
    #         }
    #         history_model.create(vals)
        
    def action_done(self):
        # if self.status == 'new':
        #     self.status = 'employed'

        # Create a record in employee.master
        self.env['techtrioz.employee.master'].create({
            'first_name': self.trainee_id.first_name,
            'last_name': self.trainee_id.last_name,
            'employee_id': self.employee_id,
            'emp_code': self.trainee_id.emp_code,
            'personal_email_id': self.trainee_id.personal_email_id,
            'linked_profile_url': self.trainee_id.linked_profile_url,
            'gender': self.trainee_id.gender,
            'dob': self.trainee_id.dob,
            'date_of_joining': self.trainee_id.date_of_joining,
            'locaton_id': self.trainee_id.locaton_id.id,
            'designation_id': self.trainee_id.designation_id.id,
            'profile_image': self.trainee_id.profile_image,
            # Add more fields as needed
        })
        
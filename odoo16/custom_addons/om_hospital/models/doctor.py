# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.osv import expression


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Hospital Doctor'

    name = fields.Char(string='Name', required=True)
    specialization = fields.Char(string='Specialization')
    contact = fields.Char(string='Contact Information')
    patients_number = fields.Integer(string='Number of Patients', compute='_compute_patients')
    patient_names = fields.Char(string='Patient Names', compute='_compute_patients')
    
    patient_ids = fields.One2many('hospital.patient','doctor',string='Patients')
    

    @api.depends('patient_ids')
    def _compute_patients(self):
        for doctor in self:
            doctor.patients_number = len(doctor.patient_ids)
            doctor.patient_names= ','.join(patient.l_name for patient in doctor.patient_ids)
      
    # def name_get(self):
    #     result = []
    #     for doctor in self:
    #         name = doctor.name or ''
    #         specialization = doctor.specialization or ''
    #         display_name = f"{name} - {specialization}"
    #         result.append((doctor.id, display_name))
    #     return result
    
    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        domain = []
        if name:
            domain= ['|', '|', ('name', operator, name), ('specialization', operator, name), ('contact', operator, name)] 
        return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)
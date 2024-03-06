# -*- coding: utf-8 -*-
from odoo import api, fields, models

class HospitalWard(models.Model):
    _name = 'hospital.ward'
    _description = 'Hospital Ward'

    name = fields.Char(string='Name', required=True)
    capacity = fields.Integer(string='Capacity')
    is_occupied = fields.Boolean(string='Is Occupied', compute='_compute_is_occupied')
    patients_number = fields.Integer(string='Number of Patients', compute='_compute_patients')
    patients_name = fields.Char(string='Patient Names', compute='_compute_patients')

    patient_ids = fields.One2many('hospital.patient','ward', string='Patients')
    
    @api.depends('patient_ids')
    def _compute_patients(self):
        for ward in self:
            ward.patients_number = len(ward.patient_ids)
            ward.patients_name = ','.join(patient.l_name for patient in ward.patient_ids)
    
    @api.depends('capacity', 'patients_number') 
    def _compute_is_occupied(self):
        for ward in self:
            ward.is_occupied = ward.capacity == ward.patients_number
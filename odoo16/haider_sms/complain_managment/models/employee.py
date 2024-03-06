# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class ComplainEmployee(models.Model):
    _name = "complain.employee"
    _description = "Complain Employee"

    id = fields.Integer(string="ID")
    name = fields.Char(string='Name')
    contact = fields.Char(string='Contact')
    age = fields.Integer(string="Age")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    designation = fields.Char(string='Designation')
    department = fields.Char(string='Department')
    complain = fields.Char(string="Complain")
    status = fields.Selection([
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('on_process', 'On_Process'),
    ], string='Status', copy=False, index=True, tracking=True, default='pending')

    image = fields.Binary(string="Image")

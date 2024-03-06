# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class TestingOne(models.Model):
    _name = "testing.two"
    _description = "Testing Two"

    complain_id = fields.Char( string='Complain_Id')
    user_name= fields.Char(string='User Name')
    designation = fields.Char(string='Designation')
    department = fields.Char(string='Department')
    complain = fields.Char(string="Complain")
    image_proof = fields.Binary(string="Image Proof")
    status = fields.Selection([
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('on_process', 'On_Process'),
    ], string='Status', copy=False, index=True, tracking=True, default='pending')


# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class TestingOne(models.Model):
    _name = "testing.one"
    _description = "Testing One"

    designation = fields.Char(string='Designation')
    department = fields.Char(string='Department')
    complain = fields.Char(string="Complain")
    image_proof = fields.Binary(string="Image Proof")
    status = fields.Selection([
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('on_process', 'On_Process'),
    ], string='Status', copy=False, index=True, tracking=True, default='pending')

    def send_to_testing_two(self):
        # Process your data or create a record directly
        testing_two_obj = self.env['testing.two'].create({
            'complain_id': self.env['ir.sequence'].next_by_code('testing.two.sequence'),
            'user_name': self.env.user.name,
            'designation': self.designation,
            'department': self.department,
            'complain': self.complain,
            'image_proof': self.image_proof,
            'status': self.status,
        })

        # Additional logic or return statement if needed
        return {
            'name': 'Send to Testing Two',
            'view_mode': 'form',
            'res_model': 'testing.two',
            'res_id': testing_two_obj.id,
            'type': 'ir.actions.act_window',
            'target': 'new',
        }


class TestingTwotransient(models.TransientModel):
    _name = 'testing.one.transient'
    _description = 'Transient Model for Testing Two'

    complain_id = fields.Char(string='Complain ID')
    user_name = fields.Char(string='User Name')
    designation = fields.Char(string='Designation')
    department = fields.Char(string='Department')
    complain = fields.Char(string="Complain")
    image_proof = fields.Binary(string="Image Proof")
    status = fields.Selection([
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('on_process', 'On_Process'),
    ], string='Status', default='pending')
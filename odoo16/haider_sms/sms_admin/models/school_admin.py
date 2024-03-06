from odoo import models, fields, api

class SchoolAdmin(models.Model):
    _name = "sms.school_admin"
    _description = "School management System , School Admin model"

    name = fields.Char(string='Admin Name', required=True)
    admin_id = fields.Char(string='Admin ID', required=True)
    contact_number = fields.Char(string='Contact Number')
    image = fields.Binary(string='Image',attachment=True)

    @api.model
    def create(self, vals):
        if vals.get('admin_id', 'New') == 'New':
            vals['admin_id']= self.env['ir.sequence'].next_by_code('sms.school_admin.sequence') or 'New'
        return super(SchoolAdmin, self).create(vals)
    
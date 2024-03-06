# models.py in your custom module 'custom_payroll'

from odoo import models, fields

class CustomPayrollSalaryRuleCategory(models.Model):
    _name = 'custom_payroll.salary_rule_category'
    _description = 'Salary Rule Category'

    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code', required=True)
    # Add other fields as needed

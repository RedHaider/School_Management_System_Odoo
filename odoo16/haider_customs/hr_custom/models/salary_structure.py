# models.py in your custom module 'custom_payroll'

from odoo import models, fields, api

class CustomPayrollSalaryStructure(models.Model):
    _name = 'custom_payroll.salary_structure'
    _description = 'Salary Structure'

    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code', required=True)
    category_id = fields.Many2one('custom_payroll.salary_rule_category', string='Salary Rule Category')
    # Add other fields as needed

    @api.model
    def create_base_salary_structure(self):
        category_vals = {
            'name': 'Basic Salary Category',
            'code': 'BASIC',
            # Add other field values as needed
        }
        category = self.env['custom_payroll.salary_rule_category'].create(category_vals)

        salary_structure_vals = {
            'name': 'Basic Salary Structure',
            'code': 'basic',
            'category_id': category.id,
            # Add other field values as needed
        }

        salary_structure = self.create(salary_structure_vals)

        # You may add additional logic to create rules, categories, etc.
        # Example:
        # rule_vals = {
        #     'name': 'Basic Salary Rule',
        #     'code': 'BASIC',
        #     'sequence': 10,
        #     'amount_select': 'code',
        #     'amount_python_compute': 'result = contract.wage',
        #     'salary_structure_id': salary_structure.id,
        #     'category_id': category.id,
        # }
        # self.env['hr.salary.rule'].create(rule_vals)

        return salary_structure

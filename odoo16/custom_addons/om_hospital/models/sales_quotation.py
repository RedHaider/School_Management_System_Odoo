# -*- coding: utf-8 -*-
from odoo import api, fields, models

class SalesQuotation(models.Model):
    _inherit = 'sale.order'  # Correct the model name from 'sales.order' to 'sale.order'

    estimated_date = fields.Date(string="Estimated Date")  # Use 'Date' instead of 'string' to define the field type

#########################################
#     Developed by: TechTrioz haider
#########################################


from odoo import models, fields, api,_
from odoo.exceptions import ValidationError

class CRMCustom(models.Model):
    _inherit = 'crm.lead'

    product_ids = fields.Many2many('product.product', string='Products', edit="inline")
    combined_info = fields.Char(string='Product Info', compute='_compute_combined_info')
    lead_line_ids = fields.One2many('crm.lead.line', 'crm_lead_id', string='Order Lines',edit="inline")

#combines the product name and code
    def _compute_combined_info(self):
        for product in self:
            product.combined_info = f"{product.default_code} - {product.name}"


    
#for sending the email using this button function  
    def send_mail_popup(self):
        template_id = self.env.ref('crm_custom.mail_template_opportunity_confirmation').id
        
        ctx = {
            'default_composition_mode': 'comment',
            'default_model': 'crm.lead',
            'default_res_id': self.id,
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
        }

        return {
            'name': 'Send Mail',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'type': 'ir.actions.act_window',
            'context': ctx,
            'target': 'new',
        }

class CustomSaleOrderLine(models.Model):
    _name = 'crm.lead.line'
    _description = 'Custom Sale Order Line'

    product_id = fields.Many2one('product.product', string='Product', required=True)
    description = fields.Text(string='Description')
    crm_lead_id = fields.Many2one('crm.lead', string='Product', required=True)
    product_image = fields.Binary(string='Design', related="product_id.product_image")
    attachment_ids = fields.Many2many('ir.attachment', string="Attachments",attachment=True,
                                  help="any attachments")
# this is the advanced version of send email
# from odoo import api, fields, models

# class CrmLead(models.Model):
#     _inherit = 'crm.lead'

#     @api.multi
#     def send_opportunity_confirmation_email(self):
#         # Ensure that the leads have email addresses
#         leads_with_email = self.filtered(lambda lead: lead.partner_id.email)

#         if leads_with_email:
#             # Load the email template
#             template_id = self.env.ref('your_module_name.mail_template_opportunity_confirmation').id

#             # Send emails for each lead
#             for lead in leads_with_email:
#                 template = self.env['mail.template'].browse(template_id)
#                 template.send_mail(lead.id, force_send=True)

#         return True
#for sending the email using this button function  
    # def send_mail_popup(self):
    #     template_id = self.env.ref('crm_custom.mail_template_opportunity_confirmation').id

    #     # Assuming that 'product_ids' is a related field pointing to the 'product.product' model
    #     products_data = []

    #     for product in self.product_ids:
    #         product_data = {
    #             'file': product.file if product.file else None,
    #             'file_name': product.file_name if product.file_name else None,
    #         }
    #         products_data.append(product_data)

    #     ctx = {
    #         'default_composition_mode': 'comment',
    #         'default_model': 'crm.lead',
    #         'default_res_id': self.id,
    #         'default_use_template': bool(template_id),
    #         'default_template_id': template_id,
    #         'default_products_data': products_data,  # Pass the list of product data
    #     }

    #     return {
    #         'name': 'Send Mail',
    #         'view_type': 'form',
    #         'view_mode': 'form',
    #         'res_model': 'mail.compose.message',
    #         'type': 'ir.actions.act_window',
    #         'context': ctx,
    #         'target': 'new',
    #     }


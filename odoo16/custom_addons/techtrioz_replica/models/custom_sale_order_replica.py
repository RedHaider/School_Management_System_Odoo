import logging
from odoo import models, fields, api, _

# Create a logger instance
_logger = logging.getLogger(__name__)

class CustomSaleOrder(models.Model):
    _name = 'custom.sale.order'
    _description = 'Custom Sales Order'
    
    name= fields.Char(
        string='Number',
        copy=False,
        readonly=True,
        index=True,
        default=lambda self: ('New')
    )
    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', ('New')) == ('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('name.sequence') or ('New')

        return super().create(vals_list)
    create_date = fields.Date(string='Creation Date', readonly=True)
    commitment_date = fields.Date(string='Commitment Date')
    expected_date = fields.Date(string='Expected Date')
    partner_id = fields.Many2one('res.partner', string='Customer', readonly=True)
    pricelist_id = fields.Many2one('product.pricelist', string='Pricelist')
    validity_date = fields.Date(string='Expiration')
    estimation_date = fields.Date(string='Estimation Date')
    payment_term_id = fields.Many2one('account.payment.term', string='Payment Terms')
    sale_order_template_id= fields.Many2one('sale.order.template',string='Quotation Template') #need to change later
    user_id = fields.Many2one('res.users', string='Sales Person', widget='many2one_avatar_user')
    team_id = fields.Char(string='Team')
    tag_ids = fields.Char(string='Tags', color='color')
    company_id = fields.Many2one('res.company', string='Company', groups='base.group_multi_company', readonly=True)
    amount_untaxed = fields.Monetary(string='Total Tax Excluded', currency_field='currency_id', compute='_compute_amount', store=True)
    amount_tax = fields.Monetary(string='Tax Total', currency_field='currency_id', compute='_compute_amount', store=True)
    amount_total = fields.Monetary(string='Total', currency_field='currency_id', compute='_compute_amount_total', store=True)
    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('sale', 'Sales Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
    ], string='Status', copy=False, index=True, tracking=True, default='draft')
    invoice_status = fields.Char(string='Invoice Status', invisible=True)
    message_needaction = fields.Char(string='Need Action', invisible=True)
    currency_id = fields.Many2one('res.currency', string='Currency', invisible=True)
    order_line = fields.One2many('custom.sale.order.line', 'order_id', string='Order Lines')

    @api.model
    def action_preview_sale_order(self):
        # Add your logic here for previewing the sale order
        # You can open a wizard, generate a report, or perform any other actions

        # For example, let's print a message in the log for demonstration purposes
        _logger.info("Sale Order Preview Button Clicked for Sale Order IDs: %s", self.ids)

        # You can return a value if needed, or perform other actions

        return True
    
    @api.depends('state')
    def action_confirm(self):
        for record in self:
            if record.state == 'draft':
                record.state = 'sent'
            elif record.state == 'sent':
                record.state = 'sale'
        return True
    
    @api.depends('order_line.price_subtotal')
    def _compute_amount_total(self):
        for order in self:
            order.amount_total = sum(order.order_line.mapped('price_subtotal'))
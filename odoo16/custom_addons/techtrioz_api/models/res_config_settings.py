# -*- coding: utf-8 -*-
#########################################
#     Developed by: TechTrioz
#########################################

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    wms_licensing_key = fields.Char(string="WMS Licensing Key", default=False)

    @api.model
    def set_values(self):
        """qr code setting field values"""
        res = super(ResConfigSettings, self).set_values()
        set_param = self.env['ir.config_parameter'].set_param
        set_param('techtrioz_api.wms_licensing_key', self.wms_licensing_key)
        return res

    @api.model
    def get_values(self):
        """qr code limit getting field values"""
        res = super(ResConfigSettings, self).get_values()
        wms_licensing_key_value = self.env['ir.config_parameter'].sudo().get_param(
            'techtrioz_api.wms_licensing_key')
        res.update(
            wms_licensing_key=wms_licensing_key_value,
        )
        return res

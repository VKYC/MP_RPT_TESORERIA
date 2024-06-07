from odoo import models, fields


class AccountMove(models.Model):
    _inherit = 'account.move'

    display_name = fields.Char(related="partner_id.display_name")
    active = fields.Boolean(related='l10n_latam_document_type_id.active')
    vat = fields.Char(related="partner_id.vat")
    type = fields.Selection(related="partner_id.type", store=True)
    actual_month = fields.Datetime(string='Date')

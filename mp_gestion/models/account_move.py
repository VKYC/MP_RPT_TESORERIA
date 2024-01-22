from odoo import api, fields, models, _
from odoo.exceptions import UserError


class AccountMove(models.Model):
    _inherit = 'account.move'

    observation_state = fields.Selection(
        selection=[("not_account", "No contabilizado"), ("account", "Contabilizado")],
        default="not_account", string="Estado de contabilizacion"
    )
    for_payroll = fields.Char()
    observation = fields.Char()
    payroll_payment_id = fields.Many2one('account.payment')
    mp_flujo_id = fields.Many2one(comodel_name="mp.flujo")
    mp_grupo_flujo_id = fields.Many2one(comodel_name="mp.grupo.flujo")
    mp_grupo_flujo_ids = fields.Many2one(comodel_name="mp.grupo.flujo")

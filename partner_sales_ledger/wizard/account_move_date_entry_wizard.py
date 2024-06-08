from odoo import models, fields


class AccountMove(models.TransientModel):
    _name = 'account.move.dates.wizard'
    _description = 'Asistente de selección de fechas contables'

    initial_date = fields.Date(string='Mes')
    final_date = fields.Date(string='Año')

    def action_confirm(self):
        month_date = self.month_date
        year_date = self.year_date

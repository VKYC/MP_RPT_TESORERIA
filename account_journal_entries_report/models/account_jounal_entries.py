from odoo import models, fields, api
from odoo.tools import date_utils


class AccountMove(models.Model):
    _inherit = 'account.move.line'

    partner_name = fields.Char(related='move_id.partner_id.display_name')
    move_line_ids = fields.One2many(related='move_id.line_ids')

    @api.model
    def read_group(self, domain, fields, groupby, offset=0, limit=None, orderby=False, lazy=True):
        if 'initial_date' in self._context and 'final_date' in self._context:
            domain += [('create_date', '>=', self._context['initial_date']),
                       ('create_date', '<=', self._context['final_date'])]

        return super(AccountMove, self).read_group(domain, fields, groupby,
                                                                 offset=offset, limit=limit,
                                                                 orderby=orderby, lazy=lazy)

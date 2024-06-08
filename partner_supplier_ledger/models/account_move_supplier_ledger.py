from odoo import models, fields, tools


class AccountMoveSupplierLedger(models.Model):
    _name = "account.move.supplier.ledger"
    _auto = False
    _description = "Report Supplier Ledger"

    date = fields.Date(string="Fecha Documento")
    invoice_date = fields.Date(string="Fecha Contable")
    sii_document_number = fields.Integer(string="Nro. Factura")
    partner_id = fields.Many2one(comodel_name="res.partner", string="Proveedor")
    l10n_latam_document_type_id = fields.Many2one(comodel_name="l10n_latam.document.type",
                                                  string="Tipo de factura recibida")
    vat = fields.Char(string="R.U.T")
    display_name = fields.Char(string="Razón Social")
    amount_untaxed = fields.Float(string="Neto")
    amount_tax = fields.Float(string="I.V.A")
    amount_residual = fields.Float(string="Total")

    def init(self):
        tools.drop_view_if_exists(self.env.cr, 'account_move_supplier_ledger')
        self.env.cr.execute("""
            CREATE OR REPLACE VIEW account_move_supplier_ledger AS (
                SELECT row_number() over () AS id,
                    am."date", am.invoice_date, am.sii_document_number, 
                    am.l10n_latam_document_type_id, lnldt."name", rp.vat, am.partner_id, 
                    rp.display_name, am.amount_untaxed, am.amount_tax, am.amount_residual
                from account_move am
                left join l10n_latam_document_type lnldt on am.l10n_latam_document_type_id = lnldt.id
                left join res_partner rp on am.partner_id = rp.id
                where facturas_conciliacion_id is not null
                and rp."type" = 'contact'
                and lnldt.active = true
                and sii_document_number != 0
            )
        """)




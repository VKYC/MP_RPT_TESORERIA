{
    'name': 'Partner Supplier Ledger',
    'version': '15.0.0.0.1',
    'summary': """ Partner Supplier Views for the Ledger """,
    'author': 'HOLDCO Networks - Baruc Alvarez',
    'website': 'HOLDCO Networks',
    'category': 'Accounting/Accounting',
    'depends': ['account', 'l10n_latam_invoice_document', 'account_move_reconcile'],
    "data": [
        "security/ir.model.access.csv",
        "wizard/account_move_date_entry_wizard.xml",
        "views/account_move_supplier_ledger_views.xml",
        "views/account_move_ledger_menuitem.xml",
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}



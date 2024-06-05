{
    'name': 'Customer / Supplier Invoices',
    'version': '15.0.0.0.0',
    'summary': """ Customer / Supplier Invoices View""",
    'author': 'Baruc Álvarez',
    'category': 'Accounting/Accounting',
    'depends': ['account', 'l10n_latam_invoice_document'],
    "data": [
        "views/account_move_views.xml",
        "views/account_move_menuitem.xml",
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}



{
    'name': 'Journal Entries Report',
    'version': '15.0.0.0.1',
    'summary': """ Report about the journal entries module """,
    'author': 'HOLDCO Networks - Baruc Alvarez',
    'website': 'HOLDCO Networks',
    'category': 'Accounting/Accounting',
    'depends': ['account'],
    "data": [
        "security/ir.model.access.csv",
        "report/account_journal_entries_report.xml",
        "wizard/account_journal_entries_date_wizard.xml",
        "views/account_journal_entries_report.xml",
        "views/account_journal_entries_menuitem.xml",
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}



# -*- coding: utf-8 -*-
{
    'name': "Mid Western Group",
    'summary': "Custom invoice, quotation and payment receipt templates for Midwestern Group",
    'description': """
        Custom Invoice, Quotation and Payment Receipt templates for Midwestern Group.
    """,
    'author': "Jil Insights",
    'website': "http://www.jilinsights.com",
    'category': 'Accounting',
    'version': '19.0.1.0.3',
    'license': 'LGPL-3',
    'depends': ['base', 'web', 'account', 'sale'],
    'data': [
        "reports/report_common.xml",
        "reports/invoice_receipt_template.xml",
        "reports/quotation_report.xml",
        "reports/quotation_report_template.xml",
        "reports/payment_receipt_template.xml",
        "reports/invoice_report.xml",
    ],
    'installable': True,
    'application': False,
}

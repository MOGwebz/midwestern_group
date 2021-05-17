# -*- coding: utf-8 -*-
{
    'name': "Mid Western Group",

    'summary': """
        Custom Invoice template for Midwestern Group """,

    'description': """
        Custom Invoice template for Midwestern Group.
    """,

    'author': "Jil Insights",
    'website': "http://www.jilinsights.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'sale'],

    # always loaded
    'data': [
        "reports/invoice_report.xml",
        # "reports/external_layout_template.xml",
        "reports/invoice_receipt_template.xml",
        "reports/quotation_report.xml",
        "reports/quotation_report_template.xml",
        #"reports/quotation_order_report_inherit.xml",
    ]
}

# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Sale Order Extension',
    'version': '1.0',
    'author': 'Myat Min Hein(M2h)',
    'category': 'Sales/Sales',
    'sequence': 60,
    'summary': 'Sales internal machinery',
    'description': "",
    'depends': ['sale','product','stock','base','sale_commission'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}

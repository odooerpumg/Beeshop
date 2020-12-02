# -*- coding: utf-8 -*-
{
    'name': "Sale Commission",

    'summary': """
        Sale Comm""",


    'category': 'Sales',
    'version': '0.1',

    'depends': [
                'sale',
                ],

    'data': [
        'security/ir.model.access.csv',
        'views/sale_commission_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}

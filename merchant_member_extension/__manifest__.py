# -*- coding: utf-8 -*-
{
    'name': "Merchant Extension",

    'summary': """
        Merchant""",


    'category': 'Base',
    'version': '0.1',

    'depends': ['base',],

    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_view.xml',
        'views/res_partner_member_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}

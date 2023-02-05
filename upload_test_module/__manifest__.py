# -*- coding: utf-8 -*-
{
    'name': "Upload Test Module",

    'summary': """
       Upload Test Module""",

    'description': """
        Upload Test Module
    """,

    'author': "Abdelhady",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
        'images': ['static/description/banner.png'],
        'installable': True,
        'auto_install': False,
}

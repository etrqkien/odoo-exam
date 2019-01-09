# -*- coding: utf-8 -*-
{
    'name': "odoo-test",

    'summary': """
        Nguyen Ngoc Tien""",

    'description': """
       Bai Test ngay 9/1/2019
    """,

    'author': "Nguyen Ngoc Tien",
    'website': "nguyenngoctien.online",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/tags.xml',
        'views/tasks.xml',
        'views/wizard.xml',
        'views/stage.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
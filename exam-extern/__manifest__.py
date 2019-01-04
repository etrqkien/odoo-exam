# -*- coding: utf-8 -*-
{
    'name': "exam-extern",

    'summary': """
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Ngoctien",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'exam-base'],

    # always loaded
    'data': [
        'views/project.xml',
        'views/task.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'application': True,
}

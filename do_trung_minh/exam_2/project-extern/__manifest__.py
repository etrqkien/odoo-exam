# -*- coding: utf-8 -*-
{
    'name': "Odoo Base Kế thừa",
    'summary': """test kế thừa""",
    'description': """
        test
    """,
    'sequence': '1',
    'author': "Trung Minh",
    'website': "https://wsas.vn",
    'category': 'Test',
    'version': '0.1',
    'depends': ['project_base'],
    'data': [
        'views/project.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/task.xml',
        'views/tags.xml',
        'views/menu.xml'
    ],
    'demo': [],
    'css': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}

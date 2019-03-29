# -*- coding: utf-8 -*-
{
    'name': "Odoo Base",
    'summary': """test""",
    'description': """
        test
    """,
    'sequence': '1',
    'author': "Trung Minh",
    'website': "https://wsas.vn",
    'category': 'Test',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'views/project.xml',
        'views/task.xml',
        'views/demo.xml',
        'views/demo_task.xml',
        'views/menu.xml'],
    'demo': [],
    'css': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}

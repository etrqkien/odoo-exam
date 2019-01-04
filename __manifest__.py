# -*- coding: utf-8 -*-
{
    'name': "Project",
    'version': '0.1',
    'author': 'Odoo SA',
    'maintainer': 'Odoo SA',
    'website': "http://www.odoo.com",
    'license': 'LGPL-3',
    'category': 'Uncategorized',

    'description': """Long description of module's purpose""",
    'summary': """Sample addon for Odoo""",
    'depends': ['base'],
    'data': [
        'views/project.xml',
        'views/task.xml',
        'views/menu.xml',

    ],
    'demo': [],
    'qweb': [],
    # 'js': ['static/src/js/first_module.js',],
    # 'css': ['static/src/css/web_example.css',],
    # 'images': ['static/description/icon.png',],
    'auto_install': False,
    'application': True,
    'installable': True,
    # 'external_dependencies': {'python' : ['usb.core','serial','qrcode']}
    # 'pre_init_hook': 'pre_init_hook',
    # 'post_init_hook': 'post_init_hook',
    # 'uninstall_hook': 'uninstall_hook',
}

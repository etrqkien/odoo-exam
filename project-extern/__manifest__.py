# -*- coding: utf-8 -*-

{
    'name': "hoang keyyy",
    'version': '0.1',
    'author': 'keyyy',
    'maintainer': 'Odoo SA',
    'website': "http://fb.com/hoangkeyyyy",
    'license': 'LGPL-3',
    'category': 'Uncategorized',
    'sequence': 1,
    'description': """bai test 1""",
    'summary': """Sample addon for Odoo""",
    'depends': ['base'],
    'data': ['view/project_extern_view.xml',
             'view/task_extern_view.xml'],
    'demo': ['demo/demo.xml'],
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
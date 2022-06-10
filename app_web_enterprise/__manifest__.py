{
    'name': "App web enterprise enhance,企业版界面增强",
    'version': '14.21.03.03',
    'author': 'Sunpop.cn',
    'category': 'Base',
    'website': 'https://www.sunpop.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'summary': """
    odoo enterprise version UI theme enhance.
    1. Add dropdown arrow to parent menu.
    2. Replace the odoo logo to your company logo in main menu.
    3. Alway show search in main menu.
    """,
    'description': """
    odoo enterprise version UI enhance.
    广州尚鹏，Sunpop.cn 的odoo模块。企业版界面增强。
    1. Add dropdown arrow to parent menu.
    多级菜单中出现箭头。
    2. Replace the odoo logo or url to your company in menu and page.
    替换主菜单界面的logo为你公司的logo。
    3. Alway show search in main menu.
    在主菜单界面让搜索可见。
    """,
    'price': 68.00,
    'currency': 'EUR',
    'depends': [
        'web_enterprise',
        'web_mobile'
    ],
    'images': [],
    'data': [
        'views/webclient_templates.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'css': [
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'js': [
    ],
    'images': ['static/description/app_web_enterprise_03.jpg'],
    'post_load': None,
    'post_init_hook': None,
    'installable': True,
    'application': True,
    'auto_install': False,
}

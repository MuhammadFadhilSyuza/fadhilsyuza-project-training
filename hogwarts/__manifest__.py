# -*- coding: utf-8 -*-
{
    'name': "hogwarts",

    'summary': """
       Odoo module for sekolah""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','report_xlsx'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/kelompokmapel_view.xml',
        'views/mapel_view.xml',
        'views/siswa_view.xml',
        'views/guru_view.xml',
        'views/jurusan_view.xml',
        'views/fasilitas_view.xml',
        'report/report.xml',
        'report/print_siswa.xml',
        'wizard/tambahpenyewa_view.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

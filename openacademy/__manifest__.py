# -*- coding: utf-8 -*-
{
    'name': "Academia",

    'summary': """
        Gestion de training para sercone""",

    'description': """
        El proposito de este módulo es aprender los entresijos de odoo 11 para poder hacer modulos para clientes y así obtener una fuente alternativa de ingresos
    """,

    'author': "César Sahagún Contreras",
    'website': "http://www.solnubex.com",


    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'César',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/openacademy.xml',
        'views/partner.xml',
        'views/session_board.xml',
        'reports/reports.xml',

    ],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
}
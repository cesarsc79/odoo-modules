# -*- coding: utf-8 -*-
{
    'name': "procuradores",

    'summary': 'Gestión de despachos de Procuradores',

    'description': 'El Procurador de los Tribunales es un profesional, Licenciado en Derecho, especializado en el procedimiento judicial, o lo que es lo mismo, en el derecho procesal. El procurador ostenta la representación de los particulares y empresas que se ven en la necesidad de acudir a los Tribunales. Tenemos la facultad, y estamos capacitados para realizar, una serie de funciones que agilizan el desarrollo del procedimiento judicial y añaden una garantía extra a nuestro cliente de la buena llevanza de su caso.',

    'author': "Cesar Sahagun",
    'website': "http://www.solnubex.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
	'base',
        'mail',
	],

    # always loaded
    'data': [
        'views/procurador.xml',
        'views/expedientes.xml',
        'views/partner.xml',
        'views/asuntos.xml',
        'views/procedimientos.xml',
        'views/actuaciones.xml',

    #    'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    #'demo': [
     #   'demo/demo.xml',
    #],

}

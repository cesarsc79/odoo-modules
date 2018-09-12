# -*- coding: utf-8 -*-
from odoo import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'


    letrado = fields.Boolean("Letrado", default=False)

    procurador = fields.Boolean("Procurador", default=False)

    juzgado = fields.Boolean("Juzgado", default=False)


#    erepresentado_ids = fields.Many2many(
#        relation='rep_exp_rel',
#        comodel_name='procurador.expediente',
#        column1='partner_id',
#        column2='expediente_id',
#        string="Representados",
#        )

#    econtrario_ids = fields.Many2many(
#        relation='con_exp_rel',
#        comodel_name='procuraor.expediente',
#        column1='partner_id',
#        column2='expediente_id',
#        string="Contrarios",
#        )

# -*- coding: utf-8 -*-

from odoo import models, fields

class Asunto(models.Model):
    _name = 'procurador.procedimiento'

    name = fields.Char(string="Nombre", required=True)

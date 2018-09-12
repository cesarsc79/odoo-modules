# -*- coding: utf-8 -*-

from odoo import models, fields

class Asunto(models.Model):
    _name = 'procurador.asunto'

    name = fields.Char(string="Nombre", required=True)

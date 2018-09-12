from odoo import models, fields, api, exceptions

class Expediente(models.Model):
    _name = 'procurador.expediente'

    name = fields.Char(string="Nombre", required=True)
    description = fields.Text()

    autos = fields.Char(
        string="Autos",
        required=True
        )

    recepcion = fields.Date(
        default=fields.Date.today
        )

    asunto_id = fields.Many2one('procurador.asunto',
        ondelete='set null', string="Asunto", index=True)

    cliente_id = fields.Many2one('res.partner',
        ondelete='set null', string="Cliente",
        domain=[('customer', '=', True)], index=True)

    procurador_id = fields.Many2one('res.partner',
        ondelete='set null', string="Procurador",
        domain=[('procurador', '=', True)], index=True)

    procedimiento_id = fields.Many2one(
	'procurador.procedimiento',
        ondelete='set null',
	string="Procedimiento",
        )

    juzgado_id = fields.Many2one('res.partner',
        ondelete='set null', string="Juzgado",
        domain=[('juzgado', '=', True)], index=True)

    representado_ids = fields.Many2many(
	relation='rep_exp_rel',
	comodel_name='res.partner',
        column1='partner_id',
        column2='expediente_id',
        string="Representados",
	)

    contrario_ids = fields.Many2many(
        relation='con_exp_rel',
        comodel_name='res.partner',
        column1='partner_id',
        column2='expediente_id',
        string="Contrarios",
        )

    letrado_ids = fields.Many2many(
        relation='let_exp_rel',
        comodel_name='res.partner',
        column1='partner_id',
        column2='letrado_id',
        string="Letrados",
        domain=[
		('letrado', '=', True)
		]
        )

    actuacion_ids = fields.One2many(
        'procurador.actuacion',
	 'expediente_id',
	 string="Actuaciones"
	)

    estado = fields.Selection(
		[('abierto','Vivo'),('cerrado','Archivado')],
		'Estado'
		)

    estado2 = fields.Selection(
		[('abierto','Pendiente'),('cerrado','Cobrado')],
		'Estado financiero'
		)

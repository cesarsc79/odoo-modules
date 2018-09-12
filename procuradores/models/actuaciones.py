from odoo import models, fields, api, exceptions

class Actuacion(models.Model):
    _name = 'procurador.actuacion'
#    _inherit = ['mail.alias.mixin', 'mail.thread', 'mail.activity.mixin', 'portal.mixin']
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char(string="Nombre", required=True)

    tipo = fields.Selection(
		[('judicial','Judicial'),('extrajudicial','Extrajudicial'),('nota','Nota')],
		'Tipo'
		)

    fecha = fields.Date(
        default=fields.Date.today
        )

    tipo_fecha = fields.Selection(
                [('plazo','Plazo'),('vencimiento','Vencimiento')],
                'Tipo Fecha'
                )

    tipo_plazo = fields.Selection(
                [('habiles','Habiles'),('naturales','Naturales'),('administrativo','Administrativo')],
                'Tipo Fecha'
                )

    vencimiento = fields.Date(
	string="Vencimiento",
	store=True,
#        compute='_get_end_date', inverse='_set_end_date'
	)


    procurador_id = fields.Many2one('res.partner',
        ondelete='set null', string="Procurador",
        domain=[('procurador', '=', True)],
	index=True
	)

    expediente_id = fields.Many2one(
	'procurador.expediente',
        ondelete='cascade',
	string="Expediente",
	required=True)

    texto = fields.Text()



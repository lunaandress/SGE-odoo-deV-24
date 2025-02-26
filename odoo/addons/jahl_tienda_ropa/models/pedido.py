from odoo import models, fields, api

class Pedido(models.Model):
    _name = 'jahl_tienda_ropa.pedido'
    _description = 'Pedido de la tienda de ropa'

    cliente_id = fields.Many2one('jahl_tienda_ropa.cliente', string='Cliente', required=True)
    producto_ids = fields.Many2many('jahl_tienda_ropa.producto', string='Productos')
    fecha_pedido = fields.Datetime(string='Fecha del Pedido', default=fields.Datetime.now)
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('procesado', 'Procesado'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado')
    ], string='Estado', default='pendiente', required=True)
    total = fields.Float(string='Total', compute='_calcular_total', store=True)

    @api.depends('producto_ids')
    def _calcular_total(self):
        """ Calcula el total del pedido sumando los precios de los productos. """
        for pedido in self:
            pedido.total = sum(p.precio for p in pedido.producto_ids)

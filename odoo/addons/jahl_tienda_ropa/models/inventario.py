from odoo import models, fields, api

class Inventario(models.Model):
    _name = 'jahl_tiendaropa.inventario'
    _description = 'Inventario de productos en la tienda de ropa'

    producto_id = fields.Many2one('jahl_tiendaropa.producto', string='Producto', required=True)
    cantidad = fields.Integer(string='Cantidad en Inventario', required=True, default=0)
    ubicacion = fields.Char(string='Ubicación en Tienda')
    fecha_actualizacion = fields.Datetime(string='Fecha de Actualización', default=fields.Datetime.now)
    imagen = fields.Image(string="Imagen del Producto")

    @api.depends('cantidad')
    def _verificar_stock(self):
        """Verifica si el stock es suficiente y si debe reponerse"""
        for record in self:
            if record.cantidad <= 5:  # Considera bajo inventario cuando haya 5 o menos unidades
                record.ubicacion = "Reponer Stock"
            else:
                record.ubicacion = "Stock Suficiente"

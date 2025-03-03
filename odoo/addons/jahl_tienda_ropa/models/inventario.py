from odoo import models, fields, api

class Inventario(models.Model):
    _name = 'jahl_tienda_ropa.inventario'
    _description = 'Inventario de productos en la tienda de ropa'

    producto_id = fields.Many2one('jahl_tienda_ropa.producto', string='Producto', required=True)
    cantidad = fields.Integer(string='Cantidad en Inventario', required=True, default=0)
    ubicacion = fields.Char(string='Ubicación en Tienda')
    fecha_actualizacion = fields.Datetime(string='Fecha de Actualización', default=fields.Datetime.now)
    imagen = fields.Image(string="Imagen del Producto")

    @api.depends('cantidad')
    def _verificar_stock(self):
        """Verifica si el stock es suficiente y si debe reponerse"""
        for record in self:
            if record.cantidad <= 5:
                record.ubicacion = "Reponer Stock"
            else:
                record.ubicacion = "Stock Suficiente"

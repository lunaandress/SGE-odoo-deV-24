from odoo import models, fields
from odoo.exceptions import UserError # type: ignore

class Producto(models.Model):
    _name = 'jahl_tienda_ropa.producto'
    _description = 'Producto de la tienda de ropa'

    
    nombre = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción')
    precio = fields.Float(string='Precio', required=True)
    stock = fields.Integer(string='Stock', default=0)
    categoria = fields.Selection(
        [('camisa', 'Camisa'), ('pantalon', 'Pantalón'), ('zapato', 'Zapato')],
        string='Categoría', default='camisa'
    )
    imagen = fields.Image(string="Imagen del Producto")

    
    def actualizar_stock(self, cantidad):
        """Método para actualizar el stock del producto"""
        self.stock += cantidad

    def reducir_stock(self, cantidad):
        """Método para reducir el stock del producto"""
        if self.stock >= cantidad:
            self.stock -= cantidad
        else:
            raise UserError('No hay suficiente stock para realizar la venta.')


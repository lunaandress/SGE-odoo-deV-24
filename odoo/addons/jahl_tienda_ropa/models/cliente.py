from odoo import models, fields

class Cliente(models.Model):
    _name = 'jahl_tienda_ropa.cliente'
    _description = 'Cliente de la tienda de ropa'

    
    nombre = fields.Char(string='Nombre', required=True)
    apellido = fields.Char(string='Apellido')
    correo = fields.Char(string='Correo Electrónico')
    telefono = fields.Char(string='Teléfono')
    direccion = fields.Text(string='Dirección')
    fecha_registro = fields.Datetime(string='Fecha de Registro', default=fields.Datetime.now)
    orden_ids = fields.One2many('jahl_tienda_ropa.pedido', 'cliente_id', string='Órdenes')

    
    def obtener_datos_completos(self):
        """Método para obtener los datos completos del cliente"""
        return f"{self.nombre} {self.apellido}, Email: {self.correo}, Tel: {self.telefono}"

    def actualizar_direccion(self, nueva_direccion):
        """Método para actualizar la dirección del cliente"""
        self.direccion = nueva_direccion

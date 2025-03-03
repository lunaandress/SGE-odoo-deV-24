# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class jahl_tienda_ropa(models.Model):
#     _name = 'jahl_tienda_ropa.jahl_tienda_ropa'
#     _description = 'jahl_tienda_ropa.jahl_tienda_ropa'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


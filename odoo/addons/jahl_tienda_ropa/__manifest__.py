# -*- coding: utf-8 -*-
{
    'name': "jahl_tiendaRopa",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/jahl_tienda_ropa_groups.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/producto_view.xml',
        'views/cliente_view.xml',
        'views/pedido_view.xml',
        'views/inventario_view.xml',
        
    ],
    'icon': '/jahl_tienda_ropa/static/description/tienda_ropa.png',  # Ruta al ícono
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}


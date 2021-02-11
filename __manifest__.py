# -*- coding: utf-8 -*-
{
    'name': "car_parts",

    'summary': """
        Add fields on products for car parts. 
        Factura Sempai""",

    'description': """
        This module adds some fields on products for car parts. 
    """,

    'author': "Sempai Space",
    'website': "http://www.sempai.space",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product',],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
#        'views/views.xml',
        'views/product_template_views.xml',
        'views/product_product_views.xml',
    ],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
}

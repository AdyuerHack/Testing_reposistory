# -*- coding: utf-8 -*-


{
     
    'name': 'machine_type',
    'version': '1.0',
    'summary': 'Machine Type Management',
    'sequence': 1,
    'description': """Módulo para la gestión de tipos de máquinas.""",
    'category': 'Management',
    'website': '',
    'depends': ['base', 'mail'],
    'data': [
        'views/machine_type_view.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
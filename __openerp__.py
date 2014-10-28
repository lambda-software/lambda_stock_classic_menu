# -*- coding: utf-8 -*-
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2012 Lambda Software (http://www.lambdasoftware.net)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

{
    'name': 'Lambda Stock Classic Menu',
    'version': '1',
    'category': 'Warehouse',
    'complexity': 'easy',
    'depends': ['stock'],
    'author': 'Lambda Software',
    'website': 'http://www.lambdasoftware.net',
    'description':
        '''
Old classic stock menus for Odoo
    ''',
    "init_xml": [],
    'update_xml': [
        'stock_view.xml',
    ],
    'demo_xml': [],
    'installable': True,
    'auto_install': False,
    'active': False,
}

##############################################################################
#
#    Copyright (C) 2015  ADHOC SA  (http://www.adhoc.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Multi Store for Accounting',
    'version': "17.0.1.1.0",
    'category': 'Accounting',
    'sequence': 14,
    'summary': '',
    'author': 'ADHOC SA',
    'website': 'www.adhoc.com.ar',
    'license': 'AGPL-3',
    'images': [
    ],
    'depends': [
        'account',
        'base_multi_store',
    ],
    'data': [
        'views/account_journal_views.xml',
        'views/account_move_line_views.xml',
        'views/account_move_views.xml',
        'views/account_payment_views.xml',
        'views/res_store_views.xml',
        'security/multi_store_security.xml',
    ],
    'demo': [
        # TODO fix demo data, perhups yml
        # 'demo/account_demo.xml',
        'demo/res_store_demo.xml',
    ],
    'installable': True,
    'auto_install': True,
    'application': False,
}

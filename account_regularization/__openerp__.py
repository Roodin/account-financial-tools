# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "Account Regularization",
    "version": "1.0",
    "author": "ACYSOS S.L.,"
              "ZikzakMedia,"
              "Odoo Community Association (OCA)",
    "contributors": [
        "Santi Argüeso <santi.argueso@gmail.com>",
        ],
    "license": "GPL-3",
    "category": "Generic Modules/Accounting",
    "description": """
    This module creates a new object in accounting,
    very similar to the account models named account.regularization.
    Within this object you can define regularization moves,
    This is, accounting moves that will automatically calculate
    the balance of a set of accounts,set it to 0 and
    transfer the difference to a new account. This is used,
    for example with tax declarations or in some countries to create
    the 'Profit and Loss' regularization
""",
    "depends": ["account"],
    "data": [
        "wizard/wizard_regularization_view.xml",
        "views/account_regularization_view.xml",
        "security/ir.model.access.csv"
    ],
    "installable": True,
}

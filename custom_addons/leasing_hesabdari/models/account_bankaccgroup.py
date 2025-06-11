from odoo import api, fields, models

class Accountbankkaccgroup(models.Model):
    _name = 'leasing_hesabdari.account_bankaccgroup'
    _rec_name = 'bankaccgroup_name'

    bankaccgroup_code = fields.Integer(size = 2)
    bankaccgroup_name = fields.Char(size = 100)


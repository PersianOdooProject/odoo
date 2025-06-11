from odoo import api, fields, models

class Accountssubdef(models.Model):
    _name = 'leasing_hesabdari.account_ssubdef'
    _rec_name = "ssubdef_name"

    ssubdef_code = fields.Char(size = 1)
    ssubdef_name = fields.Char(size = 10)

from odoo import api, fields, models

class Accountsoodziangroup(models.Model):
    _name = 'leasing_hesabdari.accountsoodzian_group'
    _rec_name = "accountsoodziangroup_name"

    accountsoodziangroup_code = fields.Integer()
    accountsoodziangroup_name = fields.Char(size = 100)
    is_selecttable = fields.Integer()

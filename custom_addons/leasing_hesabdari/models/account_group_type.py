from odoo import api, fields, models

class Accountgrouptype(models.Model):
    _name = 'leasing_hesabdari.account_group_type'
    _rec_name = "acc_group_type_name"

    acc_group_type_code = fields.Char(size = 1)
    acc_group_type_name = fields.Char(size = 20)
from odoo import api, fields, models

class Accountcontroltype(models.Model):
    _name = 'leasing_hesabdari.account_control_type'
    _rec_name = "acc_control_type_description"

    acc_control_type_code = fields.Char(size = 1)
    acc_control_type_description = fields.Char(size = 10)

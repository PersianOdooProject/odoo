from odoo import api, fields, models

class Accountmonthdefinition(models.Model):
    _name = 'leasing_hesabdari.account_monthdefinition'
    _rec_name = 'month_name'

    month_number = fields.Char(size = 2, required=True)
    month_name  = fields.Char(size = 50, required=True)


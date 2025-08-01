from odoo import api, fields, models

class Leasinginsurancebranch(models.Model):
    _name = 'leasing_leasingdata.leasing_insurancebranch'
    _rec_name = "insurancebranch_name"

    insurancebranch_oldcode = fields.Integer(size=10)
    insurancebranch_name = fields.Char(string="نام شعبه بیمه", size=50, required=True)
    ssledger_id = fields.Many2one("leasing_hesabdari.account_ssledger","حساب تفصیل")

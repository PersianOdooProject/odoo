from odoo import api, fields, models


class Recpaycashdef(models.Model):
    _name = 'leasing_recpaydata.recpay_cashdef'
    _rec_name = "cash_name"

    cash_oldcode = fields.Integer(size=10,default=0)
    cash_name = fields.Char(string="نام صندوق/تنخواه", size=50, required=True ,default="")
    ssledger_id = fields.Many2one("leasing_hesabdari.account_ssledger","حساب تفصیل")

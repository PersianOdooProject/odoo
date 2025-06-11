from odoo import api, fields, models


class Recpaycashdef(models.Model):
    _name = 'leasing_recpaydata.recpay_custdef'
    _rec_name = "cust_name"

    cust_oldcode = fields.Integer(size=10,default=0)
    cust_name = fields.Char(string="شرح هزینه", size=50, required=True ,default="")
    custaction_id = fields.Many2one("leasing_recpaydata.recpay_custaction","عملکرد هنگام ثبت فاکتور", required=True, default=3)
    ssledger_id = fields.Many2one("leasing_hesabdari.account_ssledger","حساب تفصیل")

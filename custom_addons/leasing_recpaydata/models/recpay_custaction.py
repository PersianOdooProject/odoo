from odoo import api, fields, models

class Recpaycustaction(models.Model):
    _name = 'leasing_recpaydata.recpay_custaction'
    _rec_name = "custaction_name"

    custaction_code = fields.Integer(string="کد نوع عملکرد در فاکتور", size=1)
    custaction_name = fields.Char(string="شرح نوع عملکرد در فاکتور", size=50)
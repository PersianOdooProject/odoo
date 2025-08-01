from odoo import api, fields, models


class Recpaybanktashilattype(models.Model):
    _name = 'leasing_recpaydata.recpay_banktashilattype'
    _rec_name = "tashilattype_name"

    tashilattype_code = fields.Integer(string="کد نوع تسهیلات", size=10)
    tashilattype_name = fields.Char(string="شرح نوع تسهیلات", size=50)

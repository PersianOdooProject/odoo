from odoo import api, fields, models


class Recpaybanktashilatstatus(models.Model):
    _name = 'leasing_recpaydata.recpay_banktashilatstatus'
    _rec_name = "tashilatstatus_name"

    tashilatstatus_code = fields.Integer(string="کد وضعیت تسهیلات", size=10)
    tashilatstatus_name = fields.Char(string="شرح وضعیت تسهیلات", size=50)

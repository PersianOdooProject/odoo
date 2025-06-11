from odoo import api, fields, models


class Recpaybehalf(models.Model):
    _name = 'leasing_recpaydata.recpay_behalf'
    _rec_name = "behalf_name"

    behalf_oldcode = fields.Integer(size=10,default=0)
    behalf_name = fields.Char(string="شرح بابت", size=50, required=True ,default="")
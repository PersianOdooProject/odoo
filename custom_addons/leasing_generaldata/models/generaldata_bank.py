from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Generaldatabank(models.Model):
    _name = 'leasing_generaldata.generaldata_bank'
    _rec_name = "bank_name"

    bank_oldcode = fields.Integer(string="کد بانک", size=10)
    bank_name = fields.Char(string="نام بانک", size=50, required=True)
    bank_image = fields.Image('bank_image')

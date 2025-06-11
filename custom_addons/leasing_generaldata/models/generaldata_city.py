from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Generaldatacity(models.Model):
    _name = 'leasing_generaldata.generaldata_city'
    _rec_name = "city_name"

    city_oldcode = fields.Integer(string="کد شهر", size=10)
    city_name = fields.Char(string="نام شهر", size=50, required=True)

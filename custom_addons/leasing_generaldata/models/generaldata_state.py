from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Generaldatastate(models.Model):
    _name = 'leasing_generaldata.generaldata_state'
    _rec_name = "state_name"

    state_oldcode = fields.Integer(string="کد استان", size=10)
    state_name = fields.Char(string="نام استان", size=50, required=True)
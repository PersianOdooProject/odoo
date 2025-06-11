
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Generaldatacompany_type(models.Model):
    _name = 'leasing_generaldata.generaldata_company_type'
    _rec_name = "comptype_name"

    comptype_oldcode = fields.Integer(string="کد نوع شرکت", size=10)
    comptype_name = fields.Char(string="نام نوع شرکت", size=50, required=True)
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Generaldataownershiptype(models.Model):
    _name = 'leasing_generaldata.generaldata_ownershiptype'
    _rec_name = "ownership_desc"

    ownership_oldcode = fields.Char(string="کد نوع مالکیت", size=10)
    ownership_desc = fields.Char(string="شرح نوع مالکیت", size=50, required=True)
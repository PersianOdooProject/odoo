from odoo import api, fields, models


class Generaldatagoodtype(models.Model):
    _name = 'leasing_generaldata.generaldata_goodtype'
    _rec_name = "goodtype_name"

    goodtype_oldcode = fields.Integer(string="کد قدیم نوغ کالا", size=10)
    goodtype_name = fields.Char(string="شرح نوع کالا", size=50, required=True)

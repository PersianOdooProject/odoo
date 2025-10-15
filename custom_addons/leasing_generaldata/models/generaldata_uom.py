from odoo import api, fields, models


class Generaldatauom(models.Model):
    _name = 'leasing_generaldata.generaldata_uom'
    _rec_name = "uom_name"

    uom_oldcode = fields.Integer(string="کد قدیم واحد شمارش کالا", size=10)
    uom_name = fields.Char(string="شرح واحد شمارش کالا", size=50, required=True)

from odoo import api, fields, models

class Leasinggood(models.Model):
    _name = 'leasing_leasingdata.leasing_good'
#    _rec_name = "color_name"

    good_code  = fields.Char(string="کد کالا", size=20, required=True)
    good_name = fields.Char(string="نام کالا", size=50, required=True)
    uom_id = fields.Many2one("leasing_generaldata.generaldata_uom","حساب تفصیل" , required=True)
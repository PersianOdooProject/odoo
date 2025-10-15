from odoo import api, fields, models

class Generaldatasazmantajhizat(models.Model):
    _name = 'leasing_generaldata.generaldata_sazmantajhizat'

    sazman_id = fields.Many2one("leasing_generaldata.generaldata_sazman")
    sazmantajhizat_tajhizatname = fields.Char(string="نام تجهیزات", size=100,default=" ")
    sazmantajhizat_date = fields.Date(string="تاریخ خرید" ,default=fields.Date.today())
    sazmantajhizat_country = fields.Char(string="نام کشور سازنده", size=20,default=" ")
    sazmantajhizat_tedad = fields.Integer(string="تعداد", size=10, default=0)
    sazmantajhizat_arzesh = fields.Float(string="ارزش", digits=(20,0), default=0)
from odoo import api, fields, models

class Generaldatapersontajhizat(models.Model):
    _name = 'leasing_generaldata.generaldata_persontajhizat'

    person_id = fields.Many2one("leasing_generaldata.generaldata_person")
    persontajhizat_tajhizatname = fields.Char(string="نام تجهیزات", size=100,default=" ")
    persontajhizat_date = fields.Date(string="تاریخ خرید" ,default=fields.Date.today())
    persontajhizat_country = fields.Char(string="نام کشور سازنده", size=20,default=" ")
    persontajhizat_tedad = fields.Integer(string="تعداد", size=10, default=0)
    persontajhizat_arzesh = fields.Float(string="ارزش", digits=(20,0), default=0)
from odoo import api, fields, models

class Generaldatasazmantahodat(models.Model):
    _name = 'leasing_generaldata.generaldata_sazmantahodat'

    sazman_id = fields.Many2one("leasing_generaldata.generaldata_sazman")
    tashilattype_id = fields.Many2one("leasing_generaldata.generaldata_tashilattype", required=True)
    bank_id = fields.Many2one("leasing_generaldata.generaldata_bank")
    sazmantahodat_mabtashilat = fields.Float(string="مبلغ تسهیلات", digits=(20,0), default=0)
    sazmantahodat_tardaryaft = fields.Date(string="تاریخ دریافت" ,default=fields.Date.today())
    sazmantahodat_modatpar = fields.Integer(string="مدت بازپرداخت", size=10,default=0)
    sazmantahodat_tedadaghsat = fields.Integer(string="تعداد اقساط باقیمانده", size=10,default=0)
    sazmantahodat_mabghest = fields.Float(string="مبلغ قسط ماهیانه", digits=(20,0), default=0)




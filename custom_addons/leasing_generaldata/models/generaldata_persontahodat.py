from odoo import api, fields, models

class Generaldatapersontahodat(models.Model):
    _name = 'leasing_generaldata.generaldata_persontahodat'

    person_id = fields.Many2one("leasing_generaldata.generaldata_person")
    tashilattype_id = fields.Many2one("leasing_generaldata.generaldata_tashilattype", required=True)
    bank_id = fields.Many2one("leasing_generaldata.generaldata_bank")
    persontahodat_mabtashilat = fields.Float(string="مبلغ تسهیلات", digits=(20,0), default=0)
    persontahodat_tardaryaft = fields.Date(string="تاریخ دریافت" ,default=fields.Date.today())
    persontahodat_modatpar = fields.Integer(string="مدت بازپرداخت", size=10,default=0)
    persontahodat_tedadaghsat = fields.Integer(string="تعداد اقساط باقیمانده", size=10,default=0)
    persontahodat_mabghest = fields.Float(string="مبلغ قسط ماهیانه", digits=(20,0), default=0)




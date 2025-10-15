from odoo import api, fields, models

class Leasingformolcalculation(models.Model):
    _name = 'leasing_leasingdata.leasing_formolcalculation'
    #    _rec_name = "insurance_name"

    formolcalculation_tedadmah = fields.Integer(string="مدت قرارداد", required=True, default=0)
    formolcalculation_tanavobghest = fields.Integer(string="تناوب اقساط", required=True, default=0)
    formolcalculation_tedadghest = fields.Integer(string="تعداد اقساط", required=True, default=0, readonly=True)
    formolcalculation_mabkala = fields.Float(string="مبلغ کالا", digits=(20, 0), required=True, default=0)
    formolcalculation_tashilat = fields.Float(string="مبلغ تسهیلات", digits=(20, 0), required=True, default=0)
    formolcalculation_ratesod = fields.Float(string="نرخ سود", digits=(20, 3), required=True, default=0)
    formolcalculation_sodtashilat = fields.Float(string="مبلغ سود تسهیلات", digits=(20, 0), required=True, default=0)
    formolcalculation_aslsod = fields.Float(string="مبلغ اصل و سود تسهیلات", digits=(20, 0), required=True, default=0)
    formolcalculation_pisdaryaft = fields.Float(string="مبلغ پیش دریافت شرکت", digits=(20, 0), required=True, default=0)
    formolcalculation_tolidpisdaryaft = fields.Float(string="مبلغ پیش دریافت تامین کننده", digits=(20, 0),
                                                     required=True, default=0)
    formolcalculation_roztavaghof = fields.Integer(string="تعداد روز توقف سرمایه", size=3, required=True, default=0)
    formolcalculation_mabtavaghof = fields.Float(string="مبلغ توقف سرمایه", digits=(20, 0), required=True, default=0)
    formolcalculation_sayermab1 = fields.Float(string="سایر مبالغ 1", digits=(20, 0), required=True, default=0)
    formolcalculation_sayermab2 = fields.Float(string="سایر مبالغ 2", digits=(20, 0), required=True, default=0)
    formolcalculation_sayermab3 = fields.Float(string="سایر مبالغ 3", digits=(20, 0), required=True, default=0)
    formolcalculation_ratesayer4 = fields.Float(string="نرخ سایر مبالغ 4", digits=(20, 3), required=True, default=0)
    formolcalculation_sayermab4 = fields.Float(string="سایر مبالغ 4", digits=(20, 0), required=True, default=0)
    formolcalculation_sayermab5 = fields.Float(string="سایر مبالغ 5", digits=(20, 0), required=True, default=0)
    formolcalculation_sayermab6 = fields.Float(string="سایر مبالغ 6", digits=(20, 0), required=True, default=0)
    formolcalculation_arzeshrate = fields.Float(string="نرخ ارزش افزوده", digits=(20, 3), required=True, default=0)
    formolcalculation_arzeshmab = fields.Float(string="مبلغ ارزش افزوده", digits=(20, 0), required=True, default=0)
    formolcalculation_saftehrate = fields.Float(string="نرخ سفته", digits=(20, 3), required=True, default=0)
    formolcalculation_saftehmab = fields.Float(string="مبلغ سفته", digits=(20, 0), required=True, default=0)
    formolcalculation_checkrate = fields.Float(string="نرخ چک", digits=(20, 3), required=True, default=0)
    formolcalculation_checkmab = fields.Float(string="مبلغ چک", digits=(20, 0), required=True, default=0)
    formolcalculation_ghrardadmab = fields.Float(string="مبلغ قرارداد", digits=(20, 0), required=True, default=0)
    formolcalculation_malolejaremab = fields.Float(string="مبلغ مال الاجاره", digits=(20, 0), required=True, default=0)
    formolcalculation_firstmghest = fields.Float(string="مبلغ قسط اول پایه", digits=(20, 0), required=True, default=0)
    formolcalculation_restmghest = fields.Float(string="مبلغ سایر اقساط پایه", digits=(20, 0), required=True, default=0)
    formolcalculation_lastmghest = fields.Float(string="مبلغ قسط آخر پایه", digits=(20, 0), required=True, default=0)
    formolcalculation_firstghest = fields.Float(string="مبلغ قسط اول", digits=(20, 0), required=True, default=0)
    formolcalculation_restghest = fields.Float(string="مبلغ سایر اقساط", digits=(20, 0), required=True, default=0)
    formolcalculation_lastghest = fields.Float(string="مبلغ قسط آخر", digits=(20, 0), required=True, default=0)


    def action_calculate(self):
        for rec in self:
            rec.formolcalculation_tedadghest = round(rec.formolcalculation_tedadmah/rec.formolcalculation_tanavobghest,0)
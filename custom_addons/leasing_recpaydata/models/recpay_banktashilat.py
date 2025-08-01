from odoo import api, fields, models


class Recpaybanktashilat(models.Model):
    _name = 'leasing_recpaydata.recpay_banktashilat'
    _rec_name = "tashilat_no"

    bankbranch_id = fields.Many2one("leasing_recpaydata.recpay_bankbranch","شعبه بانک")
    branchbank_name1 = fields.Char(related='bankbranch_id.bank_name1', readonly=True)
    tashilattype_id = fields.Many2one("leasing_recpaydata.recpay_banktashilattype","نوع تسیهلات")
    tashilat_name = fields.Text(string="شرح تسهیلات", required=True ,default="")
    tashilat_no = fields.Char(string="شماره تسهیلات", size=50, required=True ,default="")
    tashilatdarayft_date = fields.Date(string="تاریخ دریافت", required=True ,default=fields.Date.today())
    tashilatstart_date = fields.Date(string="تاریخ شروع", required=True ,default=fields.Date.today())
    tashilatend_date = fields.Date(string="تاریخ پایان", required=True ,default=fields.Date.today())
    tashilattasvieh_date = fields.Date(string="تاریخ تسویه")
    tedad_ghest = fields.Integer(string="تعداد اقساط", size=3, required=True ,default=1)
    tashilat_rate = fields.Float(string="نرخ تسهیلات", digits=(8,5), default=000.00000)
    masdodi_rate = fields.Float(string="نرخ مسدودی", digits=(8,5), default=000.00000)
    karmozd_rate = fields.Float(string="نرخ کارمزد", digits=(8,5), default=000.00000)
    jarimeh_rate = fields.Float(string="نرخ جریمه", digits=(8,5), default=000.00000)
    vasighe_rate = fields.Float(string="نرخ وثیقه", digits=(8,5), default=000.00000)
    moaser_rate = fields.Float(string="نرخ موثر", digits=(8,5), default=0)
    asltashilat = fields.Float(string="اصل تسهیلات", digits=(20,0), default=0)
    sodtashilat = fields.Float(string="سود تسهیلات", digits=(20,0), default=0)
    zemanatmab = fields.Float(string="مبلغ ضمانت", digits=(20,0), default=0)
    tashilatstatus_id = fields.Many2one("leasing_recpaydata.recpay_banktashilatstatus", "وضعیت تسهیلات" ,required=True)
    ssledger_id = fields.Many2one("leasing_hesabdari.account_ssledger", "حساب تفصیل")

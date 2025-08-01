from odoo import api, fields, models

class Generaldatacompanybranch(models.Model):
    _name = 'leasing_generaldata.generaldata_companybranch'
    _rec_name = "companybranch_name"

    companybranch_oldcode = fields.Integer(size=10, default=0)
    companybranch_name = fields.Char(string="نام نمایندگی", size=50, required=True)
    companybranch_prefix = fields.Char(string="پيش شماره قرارداد", size=2, required=True)
    state_id    = fields.Many2one("leasing_generaldata.generaldata_state","استان")
    state_name1 = fields.Char(related='state_id.state_name',readonly=True)
    city_id     = fields.Many2one("leasing_generaldata.generaldata_city")
    city_name1 = fields.Char(related='city_id.city_name',readonly=True)
    companybranch_address = fields.Text(string="آدرس")
    companybranch_telephone  = fields.Char(string="تلفن", size=20)
    companybranch_postcode   = fields.Char(string="كد پستی", size=10)
    companybranch_namamel = fields.Char(string="نام عامل", size=50)
    companybranch_economiccode = fields.Char(string="کد اقتصادی", size=20)
    companybranch_mobile = fields.Char(string="تلفن همراه", size=11)
    ssledger_id = fields.Many2one("leasing_hesabdari.account_ssledger")
    companybranch_image = fields.Image('companybranch_image')
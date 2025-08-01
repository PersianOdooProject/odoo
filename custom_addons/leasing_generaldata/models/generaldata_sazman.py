from odoo import api, fields, models

class Generaldatasazman(models.Model):
    _name = 'leasing_generaldata.generaldata_sazman'
    _rec_name = "sazman_name"

    sazman_oldcode = fields.Integer(size=10, default=0)
    sazman_name = fields.Char(string="نام سازمان", size=50, required=True ,)
    state_id    = fields.Many2one("leasing_generaldata.generaldata_state","استان")
    state_name1 = fields.Char(related='state_id.state_name',readonly=True)
    city_id     = fields.Many2one("leasing_generaldata.generaldata_city")
    city_name1 = fields.Char(related='city_id.city_name',readonly=True)
    sazman_address = fields.Text(string="آدرس")
    sazman_telephone  = fields.Char(string="تلفن", size=20)
    sazman_postcode   = fields.Char(string="كد پستی", size=10)
    sazman_namamel = fields.Char(string="نام نماینده", size=50)
    ssledger_id = fields.Many2one("leasing_hesabdari.account_ssledger")
    sazman_image = fields.Image('sazman_image')
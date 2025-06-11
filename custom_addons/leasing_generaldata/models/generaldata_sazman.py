from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Generaldatasazman(models.Model):
    _name = 'leasing_generaldata.generaldata_sazman'
    _rec_name = "sazman_name"

    sazman_oldcode = fields.Integer(string="کد سازمان", size=10)
    sazman_name = fields.Char(string="نام سازمان", size=50, required=True)
    state_id    = fields.Many2one("leasing_generaldata.generaldata_state")
    state_name1 = fields.Char(related='state_id.state_name',readonly=True)
    city_id     = fields.Many2one("leasing_generaldata.generaldata_city")
    city_name1 = fields.Char(related='city_id.city_name',readonly=True)

#    city_code   = fields.Char(string="كد شهر", size=3, required=True)
 #   address     = fields.Char(string="آدرس", size=50, required=True)
#    telephone   = fields.Char(string="تلفن", size=50, required=True)
#    post_code   = fields.Char(string="كد پستی", size=50, required=True)
#    ssledger    = fields.Char(string="كد تفضیل", size=50, required=True)

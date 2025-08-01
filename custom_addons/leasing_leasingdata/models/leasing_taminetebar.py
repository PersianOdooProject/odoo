from odoo import api, fields, models

class Leasingtaminetebar(models.Model):
    _name = 'leasing_leasingdata.leasing_taminetebar'
    _rec_name = "taminetebar_name"

    taminetebar_oldcode = fields.Integer(size=10)
    taminetebar_name = fields.Char(string="نام تامین کننده", size=50, required=True)
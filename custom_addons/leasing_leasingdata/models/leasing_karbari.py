from odoo import api, fields, models

class Leasingkarbari(models.Model):
    _name = 'leasing_leasingdata.leasing_karbari'
    _rec_name = "karbari_name"

    karbari_oldcode = fields.Integer(size=10)
    karbari_name = fields.Char(string="معرفی کاربری", size=50, required=True)
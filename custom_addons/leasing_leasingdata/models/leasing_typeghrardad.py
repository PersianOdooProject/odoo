from odoo import api, fields, models

class Leasingtypeghrardad(models.Model):
    _name = 'leasing_leasingdata.leasing_typeghrardad'
    _rec_name = "typeghrardad_name"

    typeghrardad_oldcode = fields.Integer(size=10)
    typeghrardad_name = fields.Char(string="معرفی انواع قرارداد", size=50, required=True)
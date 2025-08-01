from odoo import api, fields, models

class Leasingtashilattype(models.Model):
    _name = 'leasing_leasingdata.leasing_tashilattype'
    _rec_name = "tashilattype_name"

    tashilattype_oldcode = fields.Integer(size=10)
    tashilattype_name = fields.Char(string="شرح نوع تسهیلات", size=50, required=True)
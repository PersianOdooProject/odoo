from odoo import api, fields, models

class Leasinggoodcolor(models.Model):
    _name = 'leasing_leasingdata.leasing_goodcolor'
    _rec_name = "color_name"

    color_oldcode = fields.Integer(size=10)
    color_name = fields.Char(string="نام رنگ", size=50, required=True)
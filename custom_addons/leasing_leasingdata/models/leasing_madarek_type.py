from odoo import api, fields, models

class Leasingmadarek_type(models.Model):
    _name = 'leasing_leasingdata.leasing_madarek_type'
    _rec_name = "madarek_type_name"

    madarek_type_oldcode = fields.Integer(size=10)
    madarek_type_name = fields.Char(string="نام مدارک", size=50, required=True)
from odoo import api, fields, models

class Leasingmadarektype(models.Model):
    _name = 'leasing_leasingdata.leasing_madarektype'
    _rec_name = "madarektype_name"

    madarektype_oldcode = fields.Integer(size=10)
    madarektype_name = fields.Text(string="نام مدارک",required=True)
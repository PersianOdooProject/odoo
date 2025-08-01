from odoo import api, fields, models

class Leasingnavaghestype(models.Model):
    _name = 'leasing_leasingdata.leasing_navaghestype'
    _rec_name = "navaghestype_name"

    navaghestype_oldcode = fields.Integer(size=10)
    navaghestype_name = fields.Char(string="نوع نقص", size=50, required=True)
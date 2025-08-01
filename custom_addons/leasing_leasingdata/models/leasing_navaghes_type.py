from odoo import api, fields, models

class Leasingnavaghes_type(models.Model):
    _name = 'leasing_leasingdata.leasing_navaghes_type'
    _rec_name = "navaghes_type_name"

    navaghes_type_oldcode = fields.Integer(size=10)
    navaghes_type_name = fields.Char(string="نوع نقص", size=50, required=True)
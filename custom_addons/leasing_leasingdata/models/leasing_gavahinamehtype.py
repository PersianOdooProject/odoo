from odoo import api, fields, models

class Leasinggavahinamehtype(models.Model):
    _name = 'leasing_leasingdata.leasing_gavahinamehtype'
    _rec_name = "gavahinamehtype_name"

    gavahinamehtype_oldcode = fields.Integer(size=10)
    gavahinamehtype_name = fields.Char(string="شرح نوع گواهینامه", size=50, required=True)
from odoo import api, fields, models

class Leasingenseraf(models.Model):
    _name = 'leasing_leasingdata.leasing_enseraf'
    _rec_name = "enseraf_desc"

    enseraf_oldcode = fields.Integer(size=10)
    enseraf_desc = fields.Text(string="شرح دلیل انصراف", required=True)
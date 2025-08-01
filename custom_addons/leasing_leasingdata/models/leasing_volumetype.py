from odoo import api, fields, models

class Leasingvolumetype(models.Model):
    _name = 'leasing_leasingdata.leasing_volumetype'
    _rec_name = "volumetype_name"

    volumetype_oldcode = fields.Integer(size=10)
    volumetype_name = fields.Char(string="نام ظرفیت", size=50, required=True)
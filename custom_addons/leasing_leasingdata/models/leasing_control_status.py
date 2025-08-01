from odoo import api, fields, models

class Leasingcontrol_status(models.Model):
    _name = 'leasing_leasingdata.leasing_control_status'
    _rec_name = "control_status_name"

    control_status_oldcode = fields.Integer(size=10)
    control_status_name = fields.Char(string="شرح مرحله پرونده", size=50, required=True)
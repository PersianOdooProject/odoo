from odoo import api, fields, models

class Leasingcontrol_status(models.Model):
    _name = 'leasing_leasingdata.leasing_controlstatus'
    _rec_name = "controlstatus_desc"

    controlstatus_code = fields.Integer(string="کد مرحله پرونده" ,size=1 ,required=True)
    controlstatus_desc = fields.Char(string="شرح مرحله پرونده", size=50, required=True)
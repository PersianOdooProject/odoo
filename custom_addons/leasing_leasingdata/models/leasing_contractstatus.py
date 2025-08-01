from odoo import api, fields, models

class Leasingcontractstatus(models.Model):
    _name = 'leasing_leasingdata.leasing_contractstatus'
    _rec_name = "contractstatus_desc"

    contractstatus_code = fields.Integer(string="کد وضعیت قرارداد" ,size=1 , required=True)
    contractstatus_desc = fields.Char(string="شرح وضعیت قرارداد", size=50, required=True)
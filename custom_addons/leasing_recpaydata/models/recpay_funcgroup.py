from odoo import api, fields, models


class Recpayfuncgroup(models.Model):
    _name = 'leasing_recpaydata.recpay_funcgroup'
    _rec_name = "funcgroup_name"

    funcgroup_code = fields.Char(string="کد گروه فعالیت مالی" , size=1 ,required=True ,readonly=True)
    funcgroup_name = fields.Char(string="نام گروه فعالیت مالی", size=50, required=True ,readonly=True)
 #   funcdetail_list = fields.One2many("leasing_recpaydata.recpay_funcdetail" ,"funcroup_id")
from odoo import api, fields, models


class Recpaytaghvimmalicode(models.Model):
    _name = 'leasing_recpaydata.recpay_taghvimmalicode'
    _rec_name = "taghvimmalicode_name"

    @api.model
    def _get_taghvimmaligroup_list(self):
        return [('1', 'ورودی'), ('2', 'خروجی'), ('3', 'خدمات')]

    taghvimmalicode_group = fields.Selection(_get_taghvimmaligroup_list ,string="گروه اطلاعات پایه تقویم مالی" ,required=True ,default='1')
    taghvimmalicode_oldcode = fields.Integer(size=2)
    taghvimmalicode_name = fields.Char(string="شرح اطلاعات پایه تقویم مالی", size=150, required=True)
    taghvimmalicode_auto = fields.Boolean(string="ساخت اطلاعات بصورت خودکار", readonly=True, required=True, default=False)
    taghvimmalicode_default = fields.Boolean(string="پیش فرض نرم افزار", readonly=True, required=True , default=False)

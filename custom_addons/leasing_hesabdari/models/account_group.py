from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Accountgroup(models.Model):
    _name = 'leasing_hesabdari.account_group'
    _rec_names_search = ['acc_group_code' ,'acc_group_name']
    _rec_name = "acc_group_code_name"

    @api.depends('acc_group_code' ,'acc_group_name')
    def _compute_acc_group_code_name(self):
        for rec in self:
            rec.acc_group_code_name = rec.acc_group_code + ' ' + rec.acc_group_name

    acc_group_code = fields.Char(string="کد گروه حساب", size=2, required=True ,default="")
    acc_group_name = fields.Char(string="عنوان گروه حساب", size=50, required=True ,default="")
    acc_group_code_name = fields.Char(compute=_compute_acc_group_code_name, string="گروه حساب")
    acc_group_type_id = fields.Many2one("leasing_hesabdari.account_group_type", "نوع حساب", required=True)
    acc_group_type_name1 = fields.Char(related='acc_group_type_id.acc_group_type_name', readonly=True)

    _sql_constraints = [
        ('unique_accgroupcode',
         'unique(acc_group_code)',
         'کد گروه حساب نباید تکراری باشد'),

    ]

    @api.constrains('acc_group_code')
    def check_acc_group_code(self):
        for rec in self:
            if len(rec.acc_group_code) != 2  :
                raise ValidationError('کد گروه حساب باید 2 رقمی باشد')

from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class Accountssledgertype(models.Model):
    _name = 'leasing_hesabdari.account_ssledgertype'
    _rec_names_search = ['ssledgertype_code' ,'ssledgertype_name']
    _rec_name = "ssledgertype_code_name"

    @api.depends('ssledgertype_code' ,'ssledgertype_name')
    def _compute_ssledgertype_code_name(self):
        for rec in self:
            rec.ssledgertype_code_name = rec.ssledgertype_code + ' ' + rec.ssledgertype_name

    ssledgertype_code = fields.Char(string="کد نوع حساب تفصیل", size=2, required=True ,default="")
    ssledgertype_name = fields.Char(string="عنوان نوع حساب تفصیل", size=100, required=True ,default="")
    ssledgertype_code_name = fields.Char(compute=_compute_ssledgertype_code_name, string="حساب کل")

    _sql_constraints = [
        ('unique_ssledgertype_code',
         'unique(ssledgertype_code)',
         'کد نوع حساب تفصیل نباید تکراری باشد'),

    ]

@api.constrains('ssledgertype_code')
def check_ssledgertype_code(self):
    for rec in self:
        if len(rec.ssledgertype_code) != 2:
            raise ValidationError('طول کد نوع حساب تفصیل باید 2 رقمی باشد')



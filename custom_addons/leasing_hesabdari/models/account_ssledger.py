from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class Accountssledger(models.Model):
    _name = 'leasing_hesabdari.account_ssledger'
    _rec_names_search = ['ssledger' ,'ssledger_name']
    _rec_name = "ssledger_code_name"

    @api.depends('ssledger' ,'ssledger_name')
    def _compute_ssledger_code_name(self):
        for rec in self:
            rec.ssledger_code_name = rec.ssledger + ' ' + rec.ssledger_name


    ssledgertype_id = fields.Many2one("leasing_hesabdari.account_ssledgertype")
    ssledgertype_name1 = fields.Char(related='ssledgertype_id.ssledgertype_name', readonly=True)
    ssledger = fields.Char(string="کد حساب تفصیل", size=10, required=True ,default="")
    ssledger_name = fields.Char(string="عنوان حساب تفصیل", size=100, required=True ,default="")
    ssledger_code_name = fields.Char(compute=_compute_ssledger_code_name, string="حساب تفصیل")
    codemelli = fields.Char(string="کد/شناسه ملی", size=20)
    sledger_id = fields.Many2one("leasing_hesabdari.account_sledger")
    sledger_name1 = fields.Char(related='sledger_id.sledger_name', readonly=True)
    kolmoin1 = fields.Char(related='sledger_id.kolmoin', string = "کل معین مبنا در گزارش نقدینگی" ,store=True, readonly=True)
    ssledger_isactive = fields.Boolean(string="وضعیت حساب(فعال/غیرفعال)", required=True, default=True)
    ssledger_isprint = fields.Boolean(string="اعمال در گزارش نقدینگی", required=True, default=False)
    general_basedef_id = fields.Many2one("leasing_hesabdari.general_basedef", default=1)
    acc_ssledger_len1 = fields.Integer(related='general_basedef_id.acc_ssledger_len', readonly=True)

    _sql_constraints = [
        ('unique_ssledger',
         'unique(ssledger)',
         'کد حساب تفصیل نباید تکراری باشد'),

    ]


@api.constrains('ssledger')
def check_ssledger(self):
    for rec in self:
        if len(rec.ssledger) != rec.acc_ssledger_len1:
            raise ValidationError('طول حساب تفصیل نادرست می باشد')

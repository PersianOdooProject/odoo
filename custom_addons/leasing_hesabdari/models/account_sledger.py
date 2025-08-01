from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class Accountsledger(models.Model):
    _name = 'leasing_hesabdari.account_sledger'
    _rec_names_search = ['kolmoin' ,'sledger_name']
    _rec_name = "sledger_code_name"

    @api.depends('sledger')
    def _compute_kolmoin(self):
        for rec in self:
            rec.kolmoin = rec.ledger1 + rec.sledger

    @api.depends('sledger' ,'sledger_name')
    def _compute_sledger_code_name(self):
        for rec in self:
            rec.sledger_code_name = rec.ledger1 + rec.sledger + ' ' + rec.sledger_name

    ledger_id = fields.Many2one("leasing_hesabdari.account_ledger")
    ledger1 = fields.Char(related='ledger_id.ledger', readonly=True ,default="")
    ledger_name1 = fields.Char(related='ledger_id.ledger_name', readonly=True)
    ledger_code_name1 = fields.Char(related='ledger_id.ledger_code_name', store=True,readonly=True)
    accountsoodziangroup_id = fields.Many2one("leasing_hesabdari.accountsoodzian_group", required=True)
    accountsoodziangroup_name1 = fields.Char(related='accountsoodziangroup_id.accountsoodziangroup_name', readonly=True)
    sledger = fields.Char(string="کد حساب معین", size=10, required=True ,default="")
    sledger_name = fields.Char(string="عنوان حساب معین", size=100, required=True ,default="")
    sledger_code_name = fields.Char(compute=_compute_sledger_code_name, string="حساب معین")
    ssubdef_id = fields.Many2one("leasing_hesabdari.account_ssubdef", "نوع ارتباط با حساب تفصیل", required=True)
    ssubdef_name1 = fields.Char(related='ssubdef_id.ssubdef_name', readonly=True)
    acc_control_type_id = fields.Many2one("leasing_hesabdari.account_control_type", "ماهیت حساب", required=True)
    acc_control_type_description1 = fields.Char(related='acc_control_type_id.acc_control_type_description', readonly=True)
    no_ssledger = fields.Integer(string="تعداد ثبت حساب تفصیل در سند", required=True, default=1)
    get_ssledger = fields.Boolean(string="کنترل دریافت تمامی سطوح تفصیل در سند", required=True, default=True)
    sledger_isactive = fields.Boolean(string="وضعیت حساب(فعال/غیرفعال)", required=True, default=True)
    general_basedef_id = fields.Many2one("leasing_hesabdari.general_basedef", default=1)
    acc_sledger_len1 = fields.Integer(related='general_basedef_id.acc_sledger_len', readonly=True)
    kolmoin = fields.Char(compute=_compute_kolmoin, string='حساب کل و معین', store=True, readonly=True)
    ssublink_id = fields.Many2many("leasing_hesabdari.account_ssledger" ,"leasing_hesabdari_account_ssublink" ,"sledger_id" ,"ssledger_id")

    _sql_constraints = [
        ('unique_kolmoin',
         'unique(kolmoin)',
         'کد حساب کل و معین نباید تکراری باشد'),

    ]


@api.constrains('sledger')
def check_sledger(self):
    for rec in self:
        if len(rec.sledger) != rec.acc_sledger_len1:
            raise ValidationError('طول حساب معین نادرست می باشد')


@api.constrains('no_ssledger')
def check_no_ssledger(self):
    for rec in self:
        if rec.ssubdef_id != 3:
           if rec.no_ssledger < 1 or rec.no_ssledger > 3:
               raise ValidationError('عدد وارده نادرست می باشد')
        else:
            if rec.no_ssledger != 0:
                raise ValidationError('عدد وارده نادرست می باشد')


from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class Accountledger(models.Model):
    _name = 'leasing_hesabdari.account_ledger'
    _rec_names_search = ['ledger' ,'ledger_name']
    _rec_name = "ledger_code_name"

    @api.depends('ledger' ,'ledger_name')
    def _compute_ledger_code_name(self):
        for rec in self:
            rec.ledger_code_name = rec.ledger + ' ' + rec.ledger_name

    ledger = fields.Char(string="کد حساب کل", size=5, required=True ,default="")
    ledger_name = fields.Char(string="عنوان حساب کل", size=100, required=True ,default="")
    ledger_code_name = fields.Char(compute=_compute_ledger_code_name, string="حساب کل")
    acc_group_id = fields.Many2one("leasing_hesabdari.account_group", "گروه حساب", required=True)
    acc_group_code1 = fields.Char(related='acc_group_id.acc_group_code', readonly=True)
    acc_group_name1 = fields.Char(related='acc_group_id.acc_group_name', readonly=True)
    acc_group_codename1 = fields.Char(related='acc_group_id.acc_group_code_name', store=True,readonly=True)
    acc_control_type_id = fields.Many2one("leasing_hesabdari.account_control_type", "ماهیت حساب", required=True)
    acc_control_type_description1 = fields.Char(related='acc_control_type_id.acc_control_type_description', readonly=True)
    ledger_isactive = fields.Boolean(string="وضعیت حساب(فعال/غیرفعال)", required=True ,default = True)
    general_basedef_id= fields.Many2one("leasing_hesabdari.general_basedef" , default = 1)
    acc_ledger_len1 = fields.Integer(related='general_basedef_id.acc_ledger_len',readonly=True)

    _sql_constraints = [
        ('unique_ledger',
         'unique(ledger)',
         'کد حساب کل نباید تکراری باشد'),

   ]

    @api.constrains('ledger')
    def check_ledger(self):
        for rec in self:
            if len(rec.ledger) != rec.acc_ledger_len1 :
               raise ValidationError('طول حساب کل نادرست می باشد')


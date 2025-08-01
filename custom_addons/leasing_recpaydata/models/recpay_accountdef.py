from odoo import api, fields, models


class Recpayaccountdef(models.Model):
    _name = 'leasing_recpaydata.recpay_accountdef'
    _rec_names_search = ['account_no', 'account_name']
    _rec_name = "account_search_noname"

    @api.depends('account_no', 'account_name')
    def _compute_account_search_noname(self):
        for rec in self:
            rec.account_search_noname = rec.account_no + ' ' + rec.account_name

    account_oldcode = fields.Integer(size=10, default=0)
    account_no = fields.Char(string="شماره حساب", size=20, required=True, default="")
    account_name = fields.Char(string="نام حساب", size=50, required=True, default="")
    account_search_noname = fields.Char(compute=_compute_account_search_noname, string="حساب بانکی")
    account_sheba = fields.Char(string="شماره شبا", size=50, required=True, default="")
    bankbranch_id = fields.Many2one("leasing_recpaydata.recpay_bankbranch", "شعبه بانک")
    branchbank_name1 = fields.Char(related='bankbranch_id.bank_name1', readonly=True)
    branchcity_name1 = fields.Char(related='bankbranch_id.city_name1', readonly=True)
    ssledger_id = fields.Many2one("leasing_hesabdari.account_ssledger", "حساب تفصیل")

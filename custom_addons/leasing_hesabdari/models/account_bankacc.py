from odoo import api, fields, models

class Accountbankacc(models.Model):
    _name = 'leasing_hesabdari.account_bankacc'
    _rec_name = 'bankacc_name'

    bankacc_code = fields.Char(size = 5, required=True, readonly=True)
    bankacc_name = fields.Char(size = 100, required=True, readonly=True)
    bankaccgroup_id = fields.Many2one("leasing_hesabdari.account_bankaccgroup", "گروه حساب بانک مرکزی", required=True)
    sledgerlink_id = fields.Many2many("leasing_hesabdari.account_sledger" ,"leasing_hesabdari_account_bankaccsledgerlink" ,"bankacc_id" ,"sledger_id")


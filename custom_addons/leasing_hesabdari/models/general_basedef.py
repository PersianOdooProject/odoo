from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class Generalbasedef(models.Model):
    _name = 'leasing_hesabdari.general_basedef'

    def _compute_ledger_counter(self):
        for rec in self:
            lcounter = self.env['leasing_hesabdari.account_ledger'].search_count([])
            rec.ledger_total_record = lcounter

    def _compute_sledger_counter(self):
        for rec in self:
            slcounter = self.env['leasing_hesabdari.account_sledger'].search_count([])
            rec.sledger_total_record = slcounter

    def _compute_ssledger_counter(self):
        for rec in self:
            sslcounter = self.env['leasing_hesabdari.account_ssledger'].search_count([])
            rec.ssledger_total_record = sslcounter

    acc_group_len = fields.Integer(default=2)
    acc_ledger_len = fields.Integer(default=5)
    acc_sledger_len = fields.Integer(default=10)
    acc_ssledger_len = fields.Integer(default=10)
    ledger_total_record = fields.Integer(compute=_compute_ledger_counter, string="تعداد حساب کل")
    sledger_total_record = fields.Integer(compute=_compute_sledger_counter, string="تعداد حساب معین")
    ssledger_total_record = fields.Integer(compute=_compute_ssledger_counter, string="تعداد حساب تفصیل")

    @api.constrains('acc_ledger_len')
    def check_acc_ledger_len(self):
        for rec in self:
            if rec.acc_ledger_len < 1 or rec.acc_ledger_len > 5:
                raise ValidationError('طول حساب کل باید بین 1 الی 5 باشد')

    @api.constrains('acc_sledger_len')
    def check_acc_sledger_len(self):
        for rec in self:
            if rec.acc_sledger_len < 1 or rec.acc_sledger_len > 10:
                raise ValidationError('طول حساب معین باید بین 1 الی 10 باشد')

    @api.constrains('acc_ssledger_len')
    def check_acc_ssledger_len(self):
        for rec in self:
            if rec.acc_ssledger_len < 1 or rec.acc_ssledger_len > 10:
                raise ValidationError('طول حساب تفصیل باید بین 1 الی 10 باشد')

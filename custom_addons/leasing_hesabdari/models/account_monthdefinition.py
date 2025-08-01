from odoo import api, fields, models

class Accountmonthdefinition(models.Model):
    _name = 'leasing_hesabdari.account_monthdefinition'
    _rec_names_search = ['month_number' ,'month_name']
    _rec_name = "month_numname"

    @api.depends('month_number' ,'month_name')
    def _compute_month_numname(self):
        for rec in self:
            rec.month_numname = rec.month_number + ' ' + rec.month_name

    month_number = fields.Char(size = 2, required=True)
    month_name  = fields.Char(size = 50, required=True)
    month_numname = fields.Char(compute=_compute_month_numname, string="شماره و نام ماه" ,store=True)


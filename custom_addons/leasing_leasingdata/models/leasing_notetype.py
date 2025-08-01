from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Leasingnotetype(models.Model):
    _name = 'leasing_leasingdata.leasing_notetype'
    _rec_name = "notetype_name"

    notetype_code = fields.Integer(string="کد نوع فعاليت يادداشت پرونده" ,size=10)
    notetype_name = fields.Char(string="شرح نوع فعاليت يادداشت پرونده", size=50, required=True)

    _sql_constraints = [
        ('unique_notetypecode',
         'unique(notetype_code)',
         'کد نوع فعاليت يادداشت پرونده تكراري مي باشد'),

    ]

    @api.constrains('notetype_code')
    def check_notetype_code(self):
        for rec in self:
            if rec.notetype_code < 1 or rec.notetype_code > 9999999999:
                raise ValidationError('کد نوع فعاليت يادداشت پرونده باید 10 رقمی باشد')

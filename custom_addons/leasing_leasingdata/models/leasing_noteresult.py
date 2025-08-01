from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Leasingnoteresult(models.Model):
    _name = 'leasing_leasingdata.leasing_noteresult'
    _rec_name = "noteresult_name"

    noteresult_code = fields.Integer(string="کد نوع نتیجه يادداشت پرونده", size=10, required=True)
    noteresult_name = fields.Char(string="شرح نوع نتیجه يادداشت پرونده", size=50, required=True)

    _sql_constraints = [
        ('unique_noteresultcode',
         'unique(noteresult_code)',
         'کد نوع نتیجه يادداشت پرونده تكراري مي باشد'),

    ]

    @api.constrains('noteresult_code')
    def check_noteresult_code(self):
        for rec in self:
            if rec.noteresult_code < 1 or rec.noteresult_code > 9999999999:
                raise ValidationError('کد نوع نتیجه يادداشت پرونده باید 10 رقمی باشد')

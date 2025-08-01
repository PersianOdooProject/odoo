from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Leasinggoodmodel(models.Model):
    _name = 'leasing_leasingdata.leasing_goodmodel'
    _rec_names_search = ['model_code' ,'model_name']
    _rec_name = "model_code_name"

    @api.depends('model_code' ,'model_name')
    def _compute_model_code_name(self):
        for rec in self:
            rec.model_code_name = rec.model_code + ' ' + rec.model_name

    model_code = fields.Char(string="کد مدل", size=5, required=True)
    model_name = fields.Char(string="نام مدل", size=50, required=True)
    model_code_name = fields.Char(compute=_compute_model_code_name, string="مدل کالا")

    _sql_constraints = [
        ('unique_goodmodelcode',
         'unique(model_code)',
         'کد مدل کالا نباید تکراری باشد'),

    ]

    @api.constrains('model_code')
    def check_model_code(self):
        for rec in self:
            if len(rec.model_code) != 5 :
                raise ValidationError('کد مدل کالا باید 5 رقمی باشد')

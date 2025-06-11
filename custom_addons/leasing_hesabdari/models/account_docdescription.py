from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Accountdocdescription(models.Model):
    _name = 'leasing_hesabdari.account_docdescription'
    _rec_names_search = ['docdes_code' ,'docdes_text']
    _rec_name = "docdes_code_text"

    @api.depends('docdes_code' ,'docdes_text')
    def _compute_docdes_code_text(self):
        for rec in self:
            rec.docdes_code_text = rec.docdes_code + ' ' + rec.docdes_text

    docdes_code = fields.Char(string="کد شرح تکراري در سند حسابداري", size=5, required=True ,default="")
    docdes_text = fields.Char(string="متن شرح تکراري در سند حسابداري", size=100, required=True ,default="")
    docdes_code_text = fields.Char(compute=_compute_docdes_code_text, string="شرح تکراری در سند حسابداری")

    _sql_constraints = [
        ('unique_docdescode',
         'unique(docdes_code)',
         'کد شرح تکراری در سند حسابداری نباید تکراری باشد'),

    ]

    @api.constrains('docdes_code')
    def check_docdes_code(self):
        for rec in self:
            if len(rec.docdes_code) != 5 :
                raise ValidationError('کد شرح تکراري در سند حسابداري باید 5 رقمی باشد')

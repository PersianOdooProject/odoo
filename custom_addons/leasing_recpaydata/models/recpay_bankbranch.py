from odoo import api, fields, models


class Recpaybankbranch(models.Model):
    _name = 'leasing_recpaydata.recpay_bankbranch'
    _rec_names_search = ['branch_code' ,'branch_name']
    _rec_name = "branch_code_name"

    @api.depends('branch_code' ,'branch_name')
    def _compute_branch_code_name(self):
        for rec in self:
            rec.branch_code_name = rec.branch_code + ' ' + rec.branch_name

    branch_oldcode = fields.Integer(size=10,default=0)
    branch_code = fields.Char(string="کد شعبه", size=20, required=True ,default="")
    branch_name = fields.Char(string="نام شعبه", size=50, required=True ,default="")
    branch_code_name = fields.Char(compute=_compute_branch_code_name, string="شعبه بانک")
    bank_id = fields.Many2one("leasing_generaldata.generaldata_bank","بانک")
    bank_name1 = fields.Char(related='bank_id.bank_name', readonly=True)
    city_id = fields.Many2one("leasing_generaldata.generaldata_city","شهر")
    city_name1 = fields.Char(related='city_id.city_name', readonly=True)

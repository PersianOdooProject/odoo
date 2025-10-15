from odoo import api, fields, models


class Generaldatagoodgroup(models.Model):
    _name = 'leasing_generaldata.generaldata_goodgroup'
    _rec_name = "goodgroup_name"

    goodgroup_oldcode = fields.Integer(string="کد قدیم گروه کالا", size=10)
    goodgroup_name = fields.Char(string="نام گروه کالا", size=50, required=True)
    goodtype_id = fields.Many2one("leasing_generaldata.generaldata_goodtype", "نوع کالا", required=True)
    goodtype_name1 = fields.Char(related='goodtype_id.goodtype_name', readonly=True)


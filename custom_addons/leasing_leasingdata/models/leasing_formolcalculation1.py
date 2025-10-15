from odoo import api, fields, models

class Leasingformolcalculation1(models.Model):
    _name = 'leasing_leasingdata.leasing_formolcalculation1'

    formolcalculation_tedadmah = fields.Integer(string="مدت قرارداد", required=True, default=0)
    formolcalculation_mabkala = fields.Float(string="مبلغ کالا", digits=(20, 0), required=True ,default=0 ,readonly=True)
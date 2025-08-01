from odoo import api, fields, models

class Accountcalendaryear(models.Model):
    _name = 'leasing_hesabdari.account_calendaryear'
    _rec_name = 'calendaryear_shamsiyear'

    calendaryear_shamsiyear = fields.Char(size = 4, required=True, readonly=True)
    calendaryear_miladiyear = fields.Char(size = 4, required=True, readonly=True)
    calendaryear_shamsidayadd = fields.Integer(required=True, readonly=True)
    calendaryear_miladidayadd = fields.Integer(required=True, readonly=True)



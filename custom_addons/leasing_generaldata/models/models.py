# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class odoo-18.0/custom_addons/leasing_generaldata(models.Model):
#     _name = 'odoo-18.0/custom_addons/leasing_generaldata.odoo-18.0/custom_addons/leasing_generaldata'
#     _description = 'odoo-18.0/custom_addons/leasing_generaldata.odoo-18.0/custom_addons/leasing_generaldata'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


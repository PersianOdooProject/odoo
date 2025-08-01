from odoo import api, fields, models

class Accountcalendar(models.Model):
    _name = 'leasing_hesabdari.account_calendar'
    _rec_name = 'calendar_shamsidate'

    calendar_shamsidate = fields.Char(size = 10, required=True, readonly=True)
    calendar_miladidate = fields.Date(required=True, readonly=True)



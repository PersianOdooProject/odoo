from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class Accountattachment(models.Model):
    _name = 'leasing_hesabdari.account_attachment'
    _rec_name = 'attachment_name'

    attachment_name = fields.Text(required=True)

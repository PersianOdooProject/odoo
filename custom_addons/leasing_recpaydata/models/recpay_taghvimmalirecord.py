from odoo import api, fields, models
from datetime import datetime

class Recpaytaghvimmalirecord(models.Model):
    _name = 'leasing_recpaydata.recpay_taghvimmalirecord'
    _rec_name = "taghvimmalirecord_shortdesc"

    taghvimmalicode_id = fields.Many2one("leasing_recpaydata.recpay_taghvimmalicode", "اطلاعات پایه تقویم مالی")
    taghvimmalicode_group1 = fields.Selection(related='taghvimmalicode_id.taghvimmalicode_group', string="گروه اطلاعات پایه تقویم مالی",
                                 readonly=True)
    taghvimmalicode_name1 = fields.Char(related='taghvimmalicode_id.taghvimmalicode_name', string="شرح اطلاعات پایه تقویم مالی",
                                 readonly=True)
    taghvimmalirecord_date = fields.Date(string="تاریخ عملیات مالی", required=True ,default=fields.Date.today())
    taghvimmalirecord_shortdesc = fields.Char(string="شرح کوتاه عملیات مالی",required=True)
    taghvimmalirecord_description = fields.Text(string="شرح عملیات مالی")
    taghvimmalirecord_amount = fields.Float(string="مبلغ", digits=(20,0), default=0)

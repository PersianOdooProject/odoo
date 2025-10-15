from odoo import api, fields, models

class Generaldatasazmanmodiramval(models.Model):
    _name = 'leasing_generaldata.generaldata_sazmanmodiramval'

    sazman_id = fields.Many2one("leasing_generaldata.generaldata_sazman")
    sazmanmodiramval_malekname = fields.Char(string="نام و نام خانوادگی مالک", size=100,default=" ")
    sazmanmodiramval_karbari = fields.Char(string="کاربری", size=100,default=" ")
    sazmanmodiramval_masahat = fields.Float(string="مساحت", digits=(20,3), default=0)
    sazmanmodiramval_saham = fields.Float(string="سهم مالکيت", digits=(20,3), default=0)
    sazmanmodiramval_arzesh = fields.Float(string="ارزش تقريبي", digits=(20,0), default=0)
    sazmanmodiramval_address = fields.Text(string="آدرس",default=" ")
    sazmanmodiramval_description = fields.Text(string="توضيحات",default=" ")






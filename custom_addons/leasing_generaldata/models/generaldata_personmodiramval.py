from odoo import api, fields, models

class Generaldatapersonmodiramval(models.Model):
    _name = 'leasing_generaldata.generaldata_personmodiramval'

    person_id = fields.Many2one("leasing_generaldata.generaldata_person")
    personmodiramval_malekname = fields.Char(string="نام و نام خانوادگی مالک", size=100,default=" ")
    personmodiramval_karbari = fields.Char(string="کاربری", size=100,default=" ")
    personmodiramval_masahat = fields.Float(string="مساحت", digits=(20,3), default=0)
    personmodiramval_saham = fields.Float(string="سهم مالکيت", digits=(20,3), default=0)
    personmodiramval_arzesh = fields.Float(string="ارزش تقريبي", digits=(20,0), default=0)
    personmodiramval_address = fields.Text(string="آدرس",default=" ")
    personmodiramval_description = fields.Text(string="توضيحات",default=" ")






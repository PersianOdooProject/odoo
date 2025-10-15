from odoo import api, fields, models

class Generaldatasazmanshoraka(models.Model):
    _name = 'leasing_generaldata.generaldata_sazmanshoraka'

    sazman_id = fields.Many2one("leasing_generaldata.generaldata_sazman")
    sazmanshoraka_shorakaname = fields.Char(string="نام شریک/سهامدار", size=100,default=" ")
    sazmanshoraka_semat = fields.Char(string="سمت", size=100,default=" ")
    sazmanshoraka_saham = fields.Float(string="میزان سهام", digits=(20,3), default=0)
    sazmanshoraka_tahsilat = fields.Char(string="میزان تحصیلات", size=100,default=" ")
    sazmanshoraka_tajrobiat = fields.Char(string="تجربیات", size=100,default=" ")
    sazmanshoraka_description = fields.Text(string="توضیحات",default=" ")
    sazmanshoraka_isactive = fields.Boolean(string="وضعیت(فعال/غیرفعال)", required=True ,default = True)

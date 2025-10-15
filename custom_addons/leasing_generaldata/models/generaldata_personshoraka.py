from odoo import api, fields, models

class Generaldatapersonshoraka(models.Model):
    _name = 'leasing_generaldata.generaldata_personshoraka'

    person_id = fields.Many2one("leasing_generaldata.generaldata_person")
    personshoraka_shorakaname = fields.Char(string="نام شریک/سهامدار", size=100,default=" ")
    personshoraka_semat = fields.Char(string="سمت", size=100,default=" ")
    personshoraka_saham = fields.Float(string="میزان سهام", digits=(20,3), default=0)
    personshoraka_tahsilat = fields.Char(string="میزان تحصیلات", size=100,default=" ")
    personshoraka_tajrobiat = fields.Char(string="تجربیات", size=100,default=" ")
    personshoraka_description = fields.Text(string="توضیحات",default=" ")
    personshoraka_isactive = fields.Boolean(string="وضعیت(فعال/غیرفعال)", required=True ,default = True)

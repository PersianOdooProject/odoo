from odoo import api, fields, models

class Generaldatapersonazaemodirat(models.Model):
    _name = 'leasing_generaldata.generaldata_personazaemodirat'

    person_id = fields.Many2one("leasing_generaldata.generaldata_person")
    personazaemodirat_name = fields.Char(string="نام شریک/سهامدار", size=100,default=" ")
    personazaemodirat_semat = fields.Char(string="سمت", size=100,default=" ")
    personazaemodirat_tahsilat = fields.Char(string="میزان تحصیلات", size=100,default=" ")
    personazaemodirat_description = fields.Text(string="توضیحات",default=" ")
    personazaemodirat_isactive = fields.Boolean(string="وضعیت(فعال/غیرفعال)", required=True ,default = True)
    personazaemodirat_image = fields.Image('personazaemodirat_image')


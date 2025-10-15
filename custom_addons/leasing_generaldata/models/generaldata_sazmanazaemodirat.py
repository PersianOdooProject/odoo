from odoo import api, fields, models

class Generaldatasazmanazaemodirat(models.Model):
    _name = 'leasing_generaldata.generaldata_sazmanazaemodirat'

    sazman_id = fields.Many2one("leasing_generaldata.generaldata_sazman")
    sazmanazaemodirat_name = fields.Char(string="نام شریک/سهامدار", size=100,default=" ")
    sazmanazaemodirat_semat = fields.Char(string="سمت", size=100,default=" ")
    sazmanazaemodirat_tahsilat = fields.Char(string="میزان تحصیلات", size=100,default=" ")
    sazmanazaemodirat_description = fields.Text(string="توضیحات",default=" ")
    sazmanazaemodirat_isactive = fields.Boolean(string="وضعیت(فعال/غیرفعال)", required=True ,default = True)
    sazmanazaemodirat_image = fields.Image('sazmanazaemodirat_image')


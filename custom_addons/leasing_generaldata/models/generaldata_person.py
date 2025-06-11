from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Generaldataperson(models.Model):
    _name = 'leasing_generaldata.generaldata_person'
    rec_name = "person_namefamil"

    @api.depends('person_name' ,'person_famil')
    def _compute_namefamil(self):
        for rec in self:
            rec.person_namefamil = rec.person_name + ' ' + rec.person_famil

    person_oldcode = fields.Integer(string="کد اشخاص", size=10)
    person_name = fields.Char(string="نام شخص/شرکت", size=50)
    person_famil = fields.Char(string="نام خانوادگی شخص/نام شرکت", size=50)
    person_namefamil = fields.Char(compute=_compute_namefamil, string='نام و نام خانوادگی/نام شرکت', store=True, readonly=True)
    person_natcode = fields.Char(string="کد ملی شخص حقیقی", size=10)
    person_shenasemelli = fields.Char(string="شناسه ملی شخص حقوقی", size=20)
    person_image = fields.Image('person_image')
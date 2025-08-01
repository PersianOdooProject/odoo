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
    person_type = fields.Selection([('1', 'حقیقی'), ('2', 'حقوقی')] ,string="نوع شخص" ,default="1")
    person_jensiat = fields.Selection([('1', 'آقا'), ('2', 'خانم'),('3', 'شرکت')] ,string="جنسیت" ,default="1")
    person_name = fields.Char(string="نام شخص/شرکت 1", size=50)
    person_famil = fields.Char(string="نام خانوادگی شخص/شرکت 2", size=50)
    person_namefamil = fields.Char(compute=_compute_namefamil, string='نام و نام خانوادگی/نام شرکت', store=True, readonly=True)
    person_natcode = fields.Char(string="کد/شناسه ملی", size=11)
    person_namamel1 = fields.Char(string="نماینده", size=50)
    person_namamel2 = fields.Char(string="فرد کلیدی", size=50)
    person_mobile1 = fields.Char(string="تلفن همراه ۱", size=11)
    person_mobile2 = fields.Char(string="تلفن همراه ۲", size=11)
    person_economiccode = fields.Char(string="کد اقتصادی", size=20)
    ssledger_id = fields.Many2one("leasing_hesabdari.account_ssledger","حساب تفصیل")
    person_sazman = fields.Boolean(string="سازمان", required=True ,default=False)
    person_branch = fields.Boolean(string="نمایندگی", required=True ,default=False)
    person_taminkala = fields.Boolean(string="تامین کننده کالا", required=True ,default=False)
    person_tolid = fields.Boolean(string="تولید کننده", required=True ,default=False)
    person_taminetebar = fields.Boolean(string="تامین کننده اعتبار", required=True ,default=False)
    person_paygiri = fields.Boolean(string="یگیری کننده", required=True ,default=False)
    person_image = fields.Image('person_image')
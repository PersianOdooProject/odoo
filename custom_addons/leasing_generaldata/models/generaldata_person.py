from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Generaldataperson(models.Model):
    _name = 'leasing_generaldata.generaldata_person'
    _rec_name = "person_namefamil"

    @api.depends('person_name', 'person_famil')
    def _compute_namefamil(self):
        for rec in self:
            rec.person_namefamil = str(rec.person_name or '') + ' ' + str(rec.person_famil or '')

    @api.model_create_multi
    def create(self ,vals_list):
        result=super().create(vals_list)
        for rec in result:
            if rec.person_type == '2':
               rec.person_jensiat = '3'
        return result

    def write(self ,vals):
        personjensiat = ''
        if vals.get('person_jensiat'):
            personjensiat = vals.get('person_jensiat')

        if vals.get('person_type') == '2':
           personjensiat = '3'

        vals.update({'person_jensiat': personjensiat})
        res=super(Generaldataperson,self).write(vals)
        return res


    person_oldcode = fields.Integer(string="کد اشخاص", size=10, default=0)
    person_type = fields.Selection([('1', 'حقیقی'), ('2', 'حقوقی')], string="نوع شخص", default="1")
    person_jensiat = fields.Selection([('1', 'آقا'), ('2', 'خانم'), ('3', 'شرکت')], string= "جنسیت" ,default="1")
    person_name = fields.Char(string="نام شخص/شرکت 1", size=50, default=" ")
    person_famil = fields.Char(string="نام خانوادگی شخص/شرکت 2", size=50, default=" ")
    person_namefamil = fields.Char(compute=_compute_namefamil, string='نام و نام خانوادگی/نام شرکت', store=True,
                                   readonly=True)
    person_natcode = fields.Char(string="کد/شناسه ملی", size=11)
    sazman_id = fields.Many2one("leasing_generaldata.generaldata_sazman", "سازمان")
    sazman_name1 = fields.Char(related='sazman_id.sazman_name', readonly=True)
    person_namamel1 = fields.Char(string="نماینده", size=50)
    person_namamel2 = fields.Char(string="فرد کلیدی", size=50)
    person_mobile1 = fields.Char(string="تلفن همراه 1", size=11)
    person_mobile2 = fields.Char(string="تلفن همراه 2", size=11)
    person_economiccode = fields.Char(string="کد اقتصادی", size=20)
    ssledger_id = fields.Many2one("leasing_hesabdari.account_ssledger", "حساب تفصیل")
    person_branch = fields.Boolean(string="نمایندگی", required=True, default=False)
    person_taminkala = fields.Boolean(string="تامین کننده کالا", required=True, default=False)
    person_tolid = fields.Boolean(string="تولید کننده", required=True, default=False)
    person_taminetebar = fields.Boolean(string="تامین کننده اعتبار", required=True, default=False)
    person_paygiri = fields.Boolean(string="یگیری کننده", required=True, default=False)
    person_image = fields.Image('person_image')
    companybranch_prefix = fields.Char(string="پيش شماره قرارداد", size=2, default="  ")
    personaddress_list = fields.One2many("leasing_generaldata.generaldata_personaddress", "person_id")
    person_fathername = fields.Char(string="نام پدر", size=50, default="  ")
    person_shenasnameh = fields.Char(string="شماره شناسنامه", size=20, default="  ")
    person_shenasnamehserial = fields.Char(string="سریال شناسنامه", size=20, default="  ")
    person_sodorcityid = fields.Many2one("leasing_generaldata.generaldata_city", "محل صدور شناسنامه")
    sodorcity_name1 = fields.Char(related='person_sodorcityid.city_name', readonly=True)
    person_tavalodcityid = fields.Many2one("leasing_generaldata.generaldata_city", "محل تولد")
    tavalodcity_name1 = fields.Char(related='person_tavalodcityid.city_name', readonly=True)
    person_issueddate = fields.Date(string="تاریخ صدور شناسنامه", default=fields.Date.today())
    person_birthdate = fields.Date(string="تاریخ تولد", default=fields.Date.today())
    person_martialstatus = fields.Selection([('1', 'مجرد'), ('2', 'متاهل')], string="وضعیت تاهل", default="1")
    person_sponsorno = fields.Integer(string="تعداد افراد تحت تکفل", size=3, default=0)
    person_spousename = fields.Char(string="نام و نام خانوادگی همسر", size=100, default="  ")
    person_spousenatcode = fields.Char(string="کد ملی همسر", size=10, default="  ")
    person_spousesalary = fields.Float(string="میزان حقوق دریافتی همسر", digits=(20, 0), default=0)
    person_otherasset = fields.Text(string="سایر امکانات مالی و سرمایه گذاری", default=" ")
    person_otheramval = fields.Text(string="اطلاعات اموال و داراییهای موجود", default=" ")
    person_workname = fields.Char(string="نام محل کار", size=100, default="  ")
    person_worktitle = fields.Char(string="سمت", size=50, default="  ")
    person_workpersoncode = fields.Char(string="شماره شناسایی", size=20, default="  ")
    person_workrecord = fields.Char(string="سابقه کار", size=50, default="  ")
    person_worksalary = fields.Float(string="میزان حقوق یا درآمد ماهیانه", digits=(20, 0), default=0)
    person_kasrashogoghno = fields.Char(string="شماره نامه کسر از حقوق", size=20, default="  ")
    person_kasrashogoghdate = fields.Date(string="تاریخ نامه کسر از حقوق", default=fields.Date.today())
    person_workstateid = fields.Many2one("leasing_generaldata.generaldata_state", "استان")
    person_workstatename1 = fields.Char(related='person_workstateid.state_name', readonly=True)
    person_workcityid = fields.Many2one("leasing_generaldata.generaldata_city", "شهر")
    person_workcityname1 = fields.Char(related='person_workcityid.city_name', readonly=True)
    person_workaddress = fields.Text(string="آدرس", default=" ")
    person_workpostcode = fields.Char(string="کد پستی", size=10, default=" ")
    person_workshahrdari = fields.Char(string="ناحیه شهرداری", size=20, default=" ")
    person_worktelephone = fields.Char(string="تلفن", size=20, default=" ")
    person_workfax = fields.Char(string="نمابر", size=20, default=" ")
    person_workonvankasb = fields.Char(string="عنوان پروانه کسب", size=50, default="  ")
    person_workshomarehkasb = fields.Char(string="شماره پروانه کسب", size=20, default="  ")
    person_workkasbcityid = fields.Many2one("leasing_generaldata.generaldata_city", "محل صدور پروانه کسب")
    person_workcitykasbname1 = fields.Char(related='person_workkasbcityid.city_name', readonly=True)
    person_worksodorkasbdate = fields.Date(string="تاریخ صدور پروانه کسب", default=fields.Date.today())
    person_worketebarkasbdate = fields.Date(string="مدت اعتبار پروانه کسب", default=fields.Date.today())
    person_comptypeid = fields.Many2one("leasing_generaldata.generaldata_company_type", "نوع شرکت")
    person_president = fields.Char(string="نام مدیر عامل", size=50, default="  ")
    person_tasisdate = fields.Date(string="تاریخ تاسیس", default=fields.Date.today())
    person_modatsabt = fields.Char(string="مدت ثبت", size=50, default="  ")
    person_heiatmodirehno = fields.Integer(string="تعداد اعضاء هیئت مدبره", size=10, default=0)
    person_roznameh = fields.Char(string="شماره روزنامه رسمی", size=20, default="  ")
    person_rozndate = fields.Date(string="تاریخ روزنامه رسمی", default=fields.Date.today())
    person_sarmaye = fields.Float(string="سرمایه شرکت", digits=(20, 0), default=0)
    person_lastchange = fields.Text(string="آخرین تغییرات", default=" ")
    person_typework = fields.Text(string="نوع فعالیت براساس اساسنامه", default=" ")
    persontajhizat_list = fields.One2many("leasing_generaldata.generaldata_persontajhizat", "person_id")
    personshoraka_list = fields.One2many("leasing_generaldata.generaldata_personshoraka", "person_id")
    personazaemodirat_list = fields.One2many("leasing_generaldata.generaldata_personazaemodirat", "person_id")
    personmodiramval_list = fields.One2many("leasing_generaldata.generaldata_personmodiramval", "person_id")
    persontahodat_list = fields.One2many("leasing_generaldata.generaldata_persontahodat", "person_id")

    @api.constrains('person_jensiat')
    def check_person_jensiat(self):
        for rec in self:
            if rec.person_type == '1' and rec.person_jensiat == '3':
                raise ValidationError('انتخاب شرکت برای اشخاص حقیقی نادرست می باشد')

#            if rec.person_type == '2' and rec.person_jensiat != '3':
#                raise ValidationError('انتخاب آقا/خانم برای اشخاص حقوقی نادرست می باشد')


    @api.constrains('companybranch_prefix')
    def check_companybranch_prefix(self):
        for rec in self:
            if rec.person_branch == True and rec.companybranch_prefix == False:
                rec.companybranch_prefix = "  "

            if rec.person_branch == True and len(rec.companybranch_prefix.strip(" ")) != 2:
                raise ValidationError('پیش شماره قرارداد نمایندگی باید کامل وارد شود')

    @api.onchange('person_type')
    def _change_person_type(self):
        if self.person_type == '2':
            self.person_jensiat = '3'
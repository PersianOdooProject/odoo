from odoo import api, fields, models
from datetime import timedelta


class Accountaccountyear(models.Model):
    _name = 'leasing_hesabdari.account_accountyear'
#    _rec_name = 'attachment_name'

    calendaryear_id = fields.Many2one("leasing_hesabdari.account_calendaryear", "سال مالی", required=True ,default=1)
    calendaryear_shamsiyear1 = fields.Char(related='calendaryear_id.calendaryear_shamsiyear', string="سال مالی شمسی",
                                   store="True", readonly=True)
    calendaryear_miladiyear1 = fields.Char(related='calendaryear_id.calendaryear_miladiyear', string="سال مالی میلادی",
                                           store="True", readonly=True)
    calendaryear_dayadd1 = fields.Integer(related='calendaryear_id.calendaryear_shamsidayadd', string="تعداد روزهای سال",
                                           readonly=True)
    general_basedef_id= fields.Many2one("leasing_hesabdari.general_basedef" ,default=1)
    month_number1 = fields.Char(related='general_basedef_id.month_number1',readonly=True)
    startdateshamsi = fields.Char(size=10 ,string="تاریخ شروع" , reandonly=True)
    enddateshamsi = fields.Char(size=10 ,string="تاریخ پایان" , reandonly=True)
    startdatemiladi = fields.Date(string="تاریخ شروع میلادی" , store =True ,reandonly=True)
    enddatemiladi = fields.Date(string="تاریخ پایان میلادی" , store=True ,reandonly=True)
    ssledger_id = fields.Many2one("leasing_hesabdari.account_ssledger","حساب تفصیل")
    ssledger_code_name1 = fields.Char(related='ssledger_id.ssledger_code_name', string="کد و عنوان حساب تفصل", readonly=True)
    accountyear_isactive = fields.Boolean(string="وضعیت سال مالی(فعال/غیرفعال)", required=True, default=True)

    _sql_constraints = [
        ('unique_calendaryearid',
         'unique(calendaryear_id)',
         'سال مالی نباید تکراری باشد'),

    ]

    @api.onchange('calendaryear_id')
    def onchange_duration(self):
           self.startdateshamsi = self.calendaryear_shamsiyear1 + '/' + self.month_number1 + '/01'
           domain = [('calendar_shamsidate', '=', self.startdateshamsi)]
           calendar_list = self.env['leasing_hesabdari.account_calendar'].search(domain)
           self.startdatemiladi = calendar_list.calendar_miladidate
           self.enddatemiladi = self.startdatemiladi + timedelta(days = self.calendaryear_dayadd1)
           domain = [('calendar_miladidate', '=', self.enddatemiladi)]
           calendar_listmiladi = self.env['leasing_hesabdari.account_calendar'].search(domain)
           self.enddateshamsi = calendar_listmiladi.calendar_shamsidate
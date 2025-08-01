from odoo import api, fields, models


class Recpayfuncdetail(models.Model):
    _name = 'leasing_recpaydata.recpay_funcdetail'

    #    _rec_name = "funcdetail_name"

    @api.depends('basegroup_code' ,'basedetail_code')
    def _compute_basegroupdetail_code(self):
        for rec in self:
            rec.basegroupdetail_code = rec.basegroup_code + rec.basedetail_code

    @api.depends('funcgroup_code' ,'funcdetail_code')
    def _compute_funcgroupdetail_code(self):
        for rec in self:
            rec.funcgroupdetail_code = rec.funcgroup_code + rec.funcdetail_code

    @api.depends('basegroupdetail_code' ,'funcgroupdetail_code')
    def _compute_basegroupdetail_show(self):
        for rec in self:
            if rec.basegroupdetail_code == rec.funcgroupdetail_code:
               rec.basegroupdetail_show = 1
            else:
                rec.basegroupdetail_show = 0

    @api.depends('funcgroup_code' ,'funcgroup_name')
    def _compute_funcgroup_codename(self):
        for rec in self:
            rec.funcgroup_codename = rec.funcgroup_code + ' ' + rec.funcgroup_name

    @api.model
    def _get_ssledgertype_list(self):
        return [('1', 'اشخاص'), ('2', 'صندوق/تنخواه گردان'), ('3', 'حساب بانکی'), ('4', 'هزینه'), ('5', 'سازمان'),
                ('6', 'ندارد'), ('7', 'قرارداد')]

    groupcredit_id = fields.Many2one("leasing_recpaydata.recpay_funcgroup", "گروه فعالیت بستانکار", required=True)
    groupcredit_code = fields.Char(related='groupcredit_id.funcgroup_code', string="کد گروه فعالیت بستانکار",
                                   store="True", readonly=True)
    groupcredit_name = fields.Char(related='groupcredit_id.funcgroup_name', string="نام گروه فعالیت بستانکار",
                                   readonly=True)
    groupdebit_id = fields.Many2one("leasing_recpaydata.recpay_funcgroup", " گروه فعالیت بدهکار", required=True)
    groupdebit_code = fields.Char(related='groupdebit_id.funcgroup_code', string="کد گروه فعالیت بدهکار", store="True",
                                  readonly=True)
    groupdebit_name = fields.Char(related='groupdebit_id.funcgroup_name', string="نام گروه فعالیت بدهکار",
                                   readonly=True)
    basegroup_id = fields.Many2one("leasing_recpaydata.recpay_funcgroup", "گروه فعالیت پایه")
    basegroup_code = fields.Char(related='basegroup_id.funcgroup_code', string="کد گروه فعالیت پایه", store="True",
                                 readonly=True)
    basedetail_code = fields.Char(string="کد فعالیت پایه", size=2)
    basegroupdetail_code = fields.Char(compute=_compute_basegroupdetail_code, string='کد پایه فعالیت مالی', store=True, readonly=True)
    funcgroup_id = fields.Many2one("leasing_recpaydata.recpay_funcgroup", "گروه فعالیت اصلی", required=True)
    funcgroup_code = fields.Char(related='funcgroup_id.funcgroup_code', string="کد گروه فعالیت اصلی", store="True",
                                 readonly=True)
    funcgroup_name = fields.Char(related='funcgroup_id.funcgroup_name', string="نام گروه فعالیت اصلی",
                                 readonly=True)
    funcgroup_codename = fields.Char(compute=_compute_funcgroup_codename, string='کد و نام گروه فعالیت مالی', store=True ,readonly=True)
    funcdetail_code = fields.Char(string="کد فعالیت اصلی", size=2, required=True)
    funcgroupdetail_code = fields.Char(compute=_compute_funcgroupdetail_code, string='کد فعالیت مالی', store=True, readonly=True)

    ofuncgroup_id = fields.Many2one("leasing_recpaydata.recpay_funcgroup", "گروه فعالیت فرعی")
    ofuncgroup_code = fields.Char(related='ofuncgroup_id.funcgroup_code', string="کد گروه فعالیت فرعی", store="True",
                                  readonly=True)
    ofuncdetail_code = fields.Char(string="کد فعالیت فرعی", size=2)
    funcdetail_des = fields.Char(string="شرح فعالیت", size=100, required=True,readonly=True)
    sledgercredit_id = fields.Many2one("leasing_hesabdari.account_sledger")
    sledgercredit_name = fields.Char(related='sledgercredit_id.sledger_name', string="نام حساب معین بستانکار",
                                     store=True, readonly=True)
    kolmoincredit = fields.Char(related='sledgercredit_id.kolmoin', string="حساب کل و معین بستانکار", store=True,
                                readonly=True)
    ledgercredit = fields.Char(related='sledgercredit_id.ledger1', string="حساب کل بستانکار", store=True, readonly=True)
    ledgercredit_name = fields.Char(related='sledgercredit_id.ledger_name1', string="نام حساب کل بستانکار", store=True,
                                    readonly=True)
    sledgerdebit_id = fields.Many2one("leasing_hesabdari.account_sledger")
    sledgerdebit_name = fields.Char(related='sledgerdebit_id.sledger_name', string="نام حساب معین بدهکار", store=True,
                                    readonly=True)
    kolmoindebit = fields.Char(related='sledgerdebit_id.kolmoin', string="حساب کل و معین بدهکار", store=True,
                               readonly=True)
    ledgerdebit = fields.Char(related='sledgerdebit_id.ledger1', string="حساب کل بدهکار", store=True, readonly=True)
    ledgerdebit_name = fields.Char(related='sledgerdebit_id.ledger_name1', string="نام حساب کل بدهکار", store=True,
                                   readonly=True)
    ssledger1_credit = fields.Selection(_get_ssledgertype_list ,string="نوع حساب تفصیل بستانکار 1" ,default='6')
    ssledgerid1_credit = fields.Many2one("leasing_hesabdari.account_ssledger","حساب تفصیل بستانکار 1")
    ssledger1credit_code = fields.Char(related='ssledgerid1_credit.ssledger', string="کد حساب تفصل 1 بستانکار", store=True, readonly=True)
    ssledger1credit_name = fields.Char(related='ssledgerid1_credit.ssledger_name', string="عنوان حساب تفصل 1 بستانکار", store=True, readonly=True)
    ssledger2_credit = fields.Selection(_get_ssledgertype_list ,string="نوع حساب تفصیل بستانکار 2" ,default='6')
    ssledgerid2_credit = fields.Many2one("leasing_hesabdari.account_ssledger","حساب تفصیل بستانکار 2")
    ssledger2credit_code = fields.Char(related='ssledgerid1_credit.ssledger', string="کد حساب تفصل 2 بستانکار", store=True, readonly=True)
    ssledger2credit_name = fields.Char(related='ssledgerid1_credit.ssledger_name', string="عنوان حساب تفصل 2 بستانکار", store=True, readonly=True)
    ssledger3_credit = fields.Selection(_get_ssledgertype_list ,string="نوع حساب تفصیل بستانکار 3" ,default='6')
    ssledgerid3_credit = fields.Many2one("leasing_hesabdari.account_ssledger","حساب تفصیل بستانکار 3")
    ssledger3credit_code = fields.Char(related='ssledgerid1_credit.ssledger', string="کد حساب تفصل 3 بستانکار", store=True, readonly=True)
    ssledger3credit_name = fields.Char(related='ssledgerid1_credit.ssledger_name', string="عنوان حساب تفصل 3 بستانکار", store=True, readonly=True)
    ssledger1_debit = fields.Selection(_get_ssledgertype_list ,string="نوع حساب تفصیل بدهکار 1" ,default='6')
    ssledgerid1_debit = fields.Many2one("leasing_hesabdari.account_ssledger","حساب تفصیل بدهکار 1")
    ssledger1debit_code = fields.Char(related='ssledgerid1_debit.ssledger', string="کد حساب تفصل 1 بدهکار", store=True, readonly=True)
    ssledger1debit_name = fields.Char(related='ssledgerid1_debit.ssledger_name', string="عنوان حساب تفصل 1 بدهکار", store=True, readonly=True)
    ssledger2_debit = fields.Selection(_get_ssledgertype_list ,string="نوع حساب تفصیل بدهکار 2" ,default='6')
    ssledgerid2_debit = fields.Many2one("leasing_hesabdari.account_ssledger","حساب تفصیل بدهکار 2")
    ssledger2debit_code = fields.Char(related='ssledgerid1_debit.ssledger', string="کد حساب تفصل 2 بدهکار", store=True, readonly=True)
    ssledger2debit_name = fields.Char(related='ssledgerid1_debit.ssledger_name', string="عنوان حساب تفصل 2 بدهکار", store=True, readonly=True)
    ssledger3_debit = fields.Selection(_get_ssledgertype_list ,string="نوع حساب تفصیل بدهکار 3" ,default='6')
    ssledgerid3_debit = fields.Many2one("leasing_hesabdari.account_ssledger","حساب تفصیل بدهکار 3")
    ssledger3debit_code = fields.Char(related='ssledgerid1_debit.ssledger', string="کد حساب تفصل 3 بدهکار", store=True, readonly=True)
    ssledger3debit_name = fields.Char(related='ssledgerid1_debit.ssledger_name', string="عنوان حساب تفصل 3 بدهکار", store=True, readonly=True)
    basegroupdetail_show = fields.Integer(compute=_compute_basegroupdetail_show, store=True, readonly=True)

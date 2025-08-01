from odoo import api, fields, models

class Leasinginsurance(models.Model):
    _name = 'leasing_leasingdata.leasing_insurance'
    _rec_name = "insurance_name"

    insurance_oldcode = fields.Integer(size=10)
    insurance_name = fields.Char(string="نام نوع بیمه", size=50, required=True)
    insurance_useintasvieh = fields.Boolean(string="پرداختی در تسویه اعمال شود" , required=True ,defualt=True)
    insurance_amounttype = fields.Selection([('1' ,'بدهکار') ,('2' ,'بستانکار')] ,string="عملکرد مبلغ" , required=True ,defualt='1')
    insurance_calttype = fields.Selection([('1' ,'بیمه بدنه'),('2' ,'بیمه شخص ثالث'),('3','بیمه عمر'),('4','سایر بیمه ها')] ,string="گروه بیمه" , required=True ,defualt='1')
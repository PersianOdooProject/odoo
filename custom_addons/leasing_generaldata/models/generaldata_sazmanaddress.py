from odoo import api, fields, models

class Generaldatasazmanaddress(models.Model):
    _name = 'leasing_generaldata.generaldata_sazmanaddress'
#    _rec_name = "person_namefamil"

    sazmanaddress_type = fields.Char(string="نوع ادرس", size=50,default=" ")
    sazmanaddress_stateid = fields.Many2one("leasing_generaldata.generaldata_state","استان")
    state_name1 = fields.Char(related='sazmanaddress_stateid.state_name', readonly=True)
    sazmanaddress_cityid = fields.Many2one("leasing_generaldata.generaldata_city","شهر")
    city_name1 = fields.Char(related='sazmanaddress_cityid.city_name', readonly=True)
    sazmanaddress_ownershipid = fields.Many2one("leasing_generaldata.generaldata_ownershiptype","نوع مالکیت")
    ownership_desc1 = fields.Char(related='sazmanaddress_ownershipid.ownership_desc', readonly=True)
    sazmanaddress_address = fields.Text(string="آدرس",default=" ")
    sazmanaddress_postcode = fields.Char(string="کد پستی", size=10,default=" ")
    sazmanaddress_shahrdari = fields.Char(string="ناحیه شهرداری", size=20,default=" ")
    sazmanaddress_telephone1 = fields.Char(string="تلفن 1", size=20,default=" ")
    sazmanaddress_telephone2 = fields.Char(string="تلفن 2", size=20,default=" ")
    sazmanaddress_fax = fields.Char(string="نمابر", size=20, default=" ")
    sazman_id = fields.Many2one("leasing_generaldata.generaldata_sazman")


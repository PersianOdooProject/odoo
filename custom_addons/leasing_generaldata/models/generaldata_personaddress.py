from odoo import api, fields, models

class Generaldatapersonaddress(models.Model):
    _name = 'leasing_generaldata.generaldata_personaddress'
#    _rec_name = "person_namefamil"

    personaddress_type = fields.Char(string="نوع ادرس", size=50,default=" ")
    personaddress_stateid = fields.Many2one("leasing_generaldata.generaldata_state","استان")
    state_name1 = fields.Char(related='personaddress_stateid.state_name', readonly=True)
    personaddress_cityid = fields.Many2one("leasing_generaldata.generaldata_city","شهر")
    city_name1 = fields.Char(related='personaddress_cityid.city_name', readonly=True)
    personaddress_ownershipid = fields.Many2one("leasing_generaldata.generaldata_ownershiptype","نوع مالکیت")
    ownership_desc1 = fields.Char(related='personaddress_ownershipid.ownership_desc', readonly=True)
    personaddress_address = fields.Text(string="آدرس",default=" ")
    personaddress_postcode = fields.Char(string="کد پستی", size=10,default=" ")
    personaddress_shahrdari = fields.Char(string="ناحیه شهرداری", size=20,default=" ")
    personaddress_telephone1 = fields.Char(string="تلفن 1", size=20,default=" ")
    personaddress_telephone2 = fields.Char(string="تلفن 2", size=20,default=" ")
    personaddress_fax = fields.Char(string="نمابر", size=20, default=" ")
    person_id = fields.Many2one("leasing_generaldata.generaldata_person")
    personaddress_current = fields.Boolean(string="آدرس جاری", required=True ,default = False)

    @api.onchange('personaddress_current')
    def _change_personaddress_current(self):
        if self.personaddress_current:
            idcurrents = self.env['leasing_generaldata.generaldata_personaddress'].search([('id', '!=', self.id)])
            for idcurrent in idcurrents:
                idcurrent.personaddress_current = False


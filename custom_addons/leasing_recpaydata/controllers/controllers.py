# -*- coding: utf-8 -*-
# from odoo import http


# class Odoo-18.0/customAddons/leasingRecpaydata(http.Controller):
#     @http.route('/odoo-18.0/custom_addons/leasing_recpaydata/odoo-18.0/custom_addons/leasing_recpaydata', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo-18.0/custom_addons/leasing_recpaydata/odoo-18.0/custom_addons/leasing_recpaydata/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo-18.0/custom_addons/leasing_recpaydata.listing', {
#             'root': '/odoo-18.0/custom_addons/leasing_recpaydata/odoo-18.0/custom_addons/leasing_recpaydata',
#             'objects': http.request.env['odoo-18.0/custom_addons/leasing_recpaydata.odoo-18.0/custom_addons/leasing_recpaydata'].search([]),
#         })

#     @http.route('/odoo-18.0/custom_addons/leasing_recpaydata/odoo-18.0/custom_addons/leasing_recpaydata/objects/<model("odoo-18.0/custom_addons/leasing_recpaydata.odoo-18.0/custom_addons/leasing_recpaydata"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo-18.0/custom_addons/leasing_recpaydata.object', {
#             'object': obj
#         })


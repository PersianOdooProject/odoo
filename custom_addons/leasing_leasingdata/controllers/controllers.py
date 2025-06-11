# -*- coding: utf-8 -*-
# from odoo import http


# class Odoo-18.0/customAddons/leasingLeasingdata(http.Controller):
#     @http.route('/odoo-18.0/custom_addons/leasing_leasingdata/odoo-18.0/custom_addons/leasing_leasingdata', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo-18.0/custom_addons/leasing_leasingdata/odoo-18.0/custom_addons/leasing_leasingdata/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo-18.0/custom_addons/leasing_leasingdata.listing', {
#             'root': '/odoo-18.0/custom_addons/leasing_leasingdata/odoo-18.0/custom_addons/leasing_leasingdata',
#             'objects': http.request.env['odoo-18.0/custom_addons/leasing_leasingdata.odoo-18.0/custom_addons/leasing_leasingdata'].search([]),
#         })

#     @http.route('/odoo-18.0/custom_addons/leasing_leasingdata/odoo-18.0/custom_addons/leasing_leasingdata/objects/<model("odoo-18.0/custom_addons/leasing_leasingdata.odoo-18.0/custom_addons/leasing_leasingdata"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo-18.0/custom_addons/leasing_leasingdata.object', {
#             'object': obj
#         })


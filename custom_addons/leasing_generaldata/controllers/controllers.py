# -*- coding: utf-8 -*-
# from odoo import http


# class Odoo-18.0/customAddons/leasingGeneraldata(http.Controller):
#     @http.route('/odoo-18.0/custom_addons/leasing_generaldata/odoo-18.0/custom_addons/leasing_generaldata', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo-18.0/custom_addons/leasing_generaldata/odoo-18.0/custom_addons/leasing_generaldata/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo-18.0/custom_addons/leasing_generaldata.listing', {
#             'root': '/odoo-18.0/custom_addons/leasing_generaldata/odoo-18.0/custom_addons/leasing_generaldata',
#             'objects': http.request.env['odoo-18.0/custom_addons/leasing_generaldata.odoo-18.0/custom_addons/leasing_generaldata'].search([]),
#         })

#     @http.route('/odoo-18.0/custom_addons/leasing_generaldata/odoo-18.0/custom_addons/leasing_generaldata/objects/<model("odoo-18.0/custom_addons/leasing_generaldata.odoo-18.0/custom_addons/leasing_generaldata"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo-18.0/custom_addons/leasing_generaldata.object', {
#             'object': obj
#         })


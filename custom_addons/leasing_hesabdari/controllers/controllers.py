# -*- coding: utf-8 -*-
# from odoo import http


# class Leasing(http.Controller):
#     @http.route('/leasing/leasing', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/leasing/leasing/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('leasing.listing', {
#             'root': '/leasing/leasing',
#             'objects': http.request.env['leasing.leasing'].search([]),
#         })

#     @http.route('/leasing/leasing/objects/<model("leasing.leasing"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('leasing.object', {
#             'object': obj
#         })


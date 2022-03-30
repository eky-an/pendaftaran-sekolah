# -*- coding: utf-8 -*-
# from odoo import http


# class Pendaftaransekolah(http.Controller):
#     @http.route('/pendaftaransekolah/pendaftaransekolah/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pendaftaransekolah/pendaftaransekolah/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pendaftaransekolah.listing', {
#             'root': '/pendaftaransekolah/pendaftaransekolah',
#             'objects': http.request.env['pendaftaransekolah.pendaftaransekolah'].search([]),
#         })

#     @http.route('/pendaftaransekolah/pendaftaransekolah/objects/<model("pendaftaransekolah.pendaftaransekolah"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pendaftaransekolah.object', {
#             'object': obj
#         })

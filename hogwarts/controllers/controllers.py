# -*- coding: utf-8 -*-
# from odoo import http


# class Hogwarts(http.Controller):
#     @http.route('/hogwarts/hogwarts', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hogwarts/hogwarts/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hogwarts.listing', {
#             'root': '/hogwarts/hogwarts',
#             'objects': http.request.env['hogwarts.hogwarts'].search([]),
#         })

#     @http.route('/hogwarts/hogwarts/objects/<model("hogwarts.hogwarts"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hogwarts.object', {
#             'object': obj
#         })

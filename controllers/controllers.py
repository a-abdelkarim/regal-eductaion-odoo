# -*- coding: utf-8 -*-
# from odoo import http


# class Arab/regalEducation(http.Controller):
#     @http.route('/arab/regal_education/arab/regal_education', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/arab/regal_education/arab/regal_education/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('arab/regal_education.listing', {
#             'root': '/arab/regal_education/arab/regal_education',
#             'objects': http.request.env['arab/regal_education.arab/regal_education'].search([]),
#         })

#     @http.route('/arab/regal_education/arab/regal_education/objects/<model("arab/regal_education.arab/regal_education"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('arab/regal_education.object', {
#             'object': obj
#         })

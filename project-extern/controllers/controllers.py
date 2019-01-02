# -*- coding: utf-8 -*-
from odoo import http

# class Project-extern(http.Controller):
#     @http.route('/project-extern/project-extern/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project-extern/project-extern/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('project-extern.listing', {
#             'root': '/project-extern/project-extern',
#             'objects': http.request.env['project-extern.project-extern'].search([]),
#         })

#     @http.route('/project-extern/project-extern/objects/<model("project-extern.project-extern"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project-extern.object', {
#             'object': obj
#         })
# -*- coding: utf-8 -*-
from odoo import http

# class Project-base(http.Controller):
#     @http.route('/project-base/project-base/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project-base/project-base/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('project-base.listing', {
#             'root': '/project-base/project-base',
#             'objects': http.request.env['project-base.project-base'].search([]),
#         })

#     @http.route('/project-base/project-base/objects/<model("project-base.project-base"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project-base.object', {
#             'object': obj
#         })
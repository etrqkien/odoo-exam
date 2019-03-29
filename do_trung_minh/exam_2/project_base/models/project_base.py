# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProjectBase(models.Model):
    _name = 'iuh.project'
    _description = u'Quản lý Trường Đại học Công nghiệp TPHCM (IUH)'

    _rec_name = 'name'
    _translate = True

    name = fields.Char(string="Tên Project", required=True)

    manager_user_id = fields.Many2one('res.users', string='Người Quản lý', required=True)
    start_date = fields.Date(string="Ngày bắt đàu dự án", default=lambda self: fields.datetime.now())
    due_date = fields.Date(string="Ngày kết thúc dự án", default=lambda self: fields.datetime.now())
    task_ids = fields.One2many(comodel_name='iuh.tasks', inverse_name='project_id', string='Tên task',store=True)

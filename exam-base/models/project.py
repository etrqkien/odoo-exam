# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Project(models.Model):
    _name = 'exam.project'
    _description = 'Exam Project'

    name = fields.Char("Tên project")
    manager_user_id = fields.Many2one(comodel_name="res.users", string="nguoi quản lý", )
    start_date = fields.Datetime("Ngày bắt đầu")
    due_date = fields.Datetime("Ngày kết thúc")
    task_ids = fields.One2many("exam.task", inverse_name="project_id", string="Danh sách task của dự án")

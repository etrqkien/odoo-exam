# -*- coding: utf8 -*-
from odoo import fields, models, api

class ExamProject(models.Model):
    _name = "exam.project"

    name = fields.Char("Tên Dự Án")
    manager_user_id = fields.Many2one(comodel_name="res.users", string="Người quản lí")
    start_date = fields.Date("Ngày bắt đầu dự ")
    due_date = fields.Date("Ngày kết thúc dự án")
    task_ids = fields.One2many("exam.task", "project_id", "Danh sách task")


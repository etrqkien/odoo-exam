# -*- coding: utf-8 -*-

from odoo import fields, models, api, exceptions


class Task(models.Model):
    _name = 'exam.task'
    _description = 'Exam Task'

    name = fields.Char("Tên task")
    user_id = fields.Many2one(comodel_name="res.users", string="User thực hiện task" )
    start_date = fields.Date("Ngày bắt đầu")
    due_date = fields.Date("Ngày kết thúc")
    project_id = fields.Many2one(comodel_name="exam.project", string="Project" )
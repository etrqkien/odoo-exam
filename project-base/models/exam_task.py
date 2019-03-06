# -*- coding: utf8 -*-
from odoo import fields, models, api

class ExamTask(models.Model):
    _name = "exam.task"

    name = fields.Char("Tên Task")
    user_id = fields.Many2one(comodel_name="res.users", string="User thực hiện Task")
    start_date = fields.Date("Ngày bắt đầu task")
    due_date = fields.Date("Ngày kết thúc task")
    project_id = fields.Many2one(comodel_name="exam.project", string="Id project")


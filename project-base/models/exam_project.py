# -*- coding: utf-8 -*-

from odoo import fields, models, api, exceptions


class ExamProject(models.Model):
    _name = 'exam.project'
    _description = 'Exam Project'

    name = fields.Char("Tên project")
    manager_user_id = fields.Many2one(comodel_name="res.users", string="User quản lý", required=False, )
    start_date = fields.Date("Ngày bắt đầu")
    due_date = fields.Date("Ngày kết thúc")
    task_ids = fields.One2many(comodel_name="exam.task",
                               inverse_name="project_id",
                               string="Danh sách task của dự án",
                               required=False, )

    @api.multi
    @api.constrains("start_date", "due_date")
    def date_validate(self):
        for rec in self:
            if rec.start_date and rec.due_date:
                if rec.start_date > rec.due_date:
                    raise exceptions.ValidationError(u"Ngày kết thúc không thể diễn ra trước ngày bắt đầu!")

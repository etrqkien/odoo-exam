# -*- coding: utf-8 -*-

from odoo import fields, models, api, exceptions


class ExamTask(models.Model):
    _name = 'exam.task'
    _description = 'Exam Task'

    name = fields.Char("Tên task")
    user_id = fields.Many2one(comodel_name="res.users", string="User thực hiện task", required=False, )
    start_date = fields.Datetime("Ngày giờ bắt đầu")
    due_date = fields.Datetime("Ngày giờ kết thúc")
    project_id = fields.Many2one(comodel_name="exam.project", string="Project", required=False, )

    @api.constrains("start_date", "due_date")
    def date_validate(self):
        if self.start_date and self.due_date:
            if self.start_date > self.due_date:
                raise exceptions.ValidationError(u"Ngày giờ kết thúc không thể diễn ra trước ngày giờ bắt đầu!")

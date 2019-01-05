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

    @api.multi
    @api.constrains("start_date", "due_date")
    def date_validate(self):
        for rec in self:
            if rec.start_date and rec.due_date:
                if rec.start_date > rec.due_date:
                    raise exceptions.ValidationError(u"Ngày giờ kết thúc không thể diễn ra trước ngày giờ bắt đầu!")

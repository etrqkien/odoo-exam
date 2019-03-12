# -*- coding: utf8 -*-
from odoo import fields, api, models
from datetime import datetime

class ExtExamProject(models.Model):
    _inherit = "exam.project"

    status = fields.Selection([("1", "init"),
                               ("2", "finish"),
                               ("3", "fail")], "Status", default="1")
    working_status = fields.Selection([("1", "Chưa bắt đầu"),
                                       ("2", "Đang hoạt động"),
                                       ("3", "Đã kết thúc")], "Working Status", compute="_compute_working_status")

    @api.multi
    @api.depends("start_date", "due_date")
    def _compute_working_status(self):
        day_now = fields.Date.from_string(fields.Date.today())

        for item in self:
            if item.start_date and item.due_date:
                start_date2str = fields.Date.from_string(item.start_date)
                due_date2str = fields.Date.from_string(item.due_date)

                if day_now < start_date2str:
                    item.working_status = "1"
                elif day_now > start_date2str and day_now < due_date2str:
                    item.working_status = "2"
                elif day_now > due_date2str:
                    item.working_status = "3"

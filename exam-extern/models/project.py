# -*- coding: utf-8 -*-
from odoo import models, fields, api
import datetime


class project(models.Model):
    _inherit = 'exam.project'
    working_status = fields.Selection(
        [('chua', 'Chưa Bắt đầu'), ('dang', 'đang hoạt động'), ('ketthuc', 'Đã kết thúc')], default="chua",
        compute='working_status_compute')

    @api.depends("start_date", "due_date")
    def working_status_compute(self):
        dt = datetime.datetime.now()
        now = dt.strftime("%Y-%m-%d")
        if (str(self.start_date) > now):
            self.working_status = 'chua'
        elif str(self.start_date) < now < str(self.due_date):
            self.working_status = 'dang'
        else:
            self.working_status = 'ketthuc'

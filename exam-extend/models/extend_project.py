# -*- coding: utf-8 -*-

from odoo import fields, models, api

import datetime


class ExamProject(models.Model):
    _inherit = 'exam.project'

    status = fields.Selection(string="Status",
                              selection=[('init', 'Init'),
                                         ('finish', 'Finish'),
                                         ('fail', 'Fail')],
                              default='init',
                              )
    working_status = fields.Selection(string="Working status",
                                      selection=[('chua', 'Chưa bắt đầu'),
                                                 ('dang', 'Đang hoạt động'),
                                                 ('da', 'Đã kết thúc')],
                                      compute='working_status_compute',
                                      )

    @api.depends("start_date", "due_date")
    def working_status_compute(self):

        if (self.start_date is not False) & (self.due_date is not False):
            sdate = datetime.date(*[int(i) for i in self.start_date.split("-")])
            ddate = datetime.date(*[int(i) for i in self.due_date.split("-")])
            if datetime.date.today() < sdate:
                self.working_status = 'chua'
            elif sdate <= datetime.date.today() <= ddate:
                self.working_status = 'dang'
            else:
                self.working_status = 'da'
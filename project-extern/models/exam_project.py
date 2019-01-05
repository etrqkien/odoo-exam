# -*- coding: utf-8 -*-

from odoo import fields, models, api

# import datetime


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

        if self.start_date and self.due_date:

            sdate = fields.Date.from_string(self.start_date)
            ddate = fields.Date.from_string(self.due_date)
            today = fields.Date.from_string(fields.Date.today())

            if today < sdate:
                self.working_status = 'chua'
            elif sdate <= today <= ddate:
                self.working_status = 'dang'
            else:
                self.working_status = 'da'

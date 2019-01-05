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

    @api.multi
    @api.depends("start_date", "due_date")
    def working_status_compute(self):

        for rec in self:
            if rec.start_date and rec.due_date:

                sdate = fields.Date.from_string(rec.start_date)
                ddate = fields.Date.from_string(rec.due_date)
                today = fields.Date.from_string(fields.Date.today())

                if today < sdate:
                    rec.working_status = 'chua'
                elif sdate <= today <= ddate:
                    rec.working_status = 'dang'
                else:
                    rec.working_status = 'da'

            rec.working_status = 'chua'
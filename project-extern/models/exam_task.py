# -*- coding: utf-8 -*-

from odoo import fields, models, api
import datetime


class ExamTask(models.Model):
    _inherit = 'exam.task'

    status = fields.Selection(string="Status",
                              selection=[('init', 'Init'),
                                         ('inprogress', 'In Progress'),
                                         ('finish', 'Finish')],
                              default='init',
                              )
    working_status = fields.Selection(string="Working status",
                                      selection=[('not', 'Not Start'),
                                                 ('in', 'In Working Time'),
                                                 ('finish', 'Finish'),
                                                 ('over', 'Over Deadline')],

                                      compute='working_status_compute',
                                      )

    @api.depends("start_date", "due_date", "status")
    def working_status_compute(self):
        if (self.start_date is not False) & (self.due_date is not False):
            sdate = datetime.date(*[int(i) for i in self.start_date.split("-")])
            ddate = datetime.date(*[int(i) for i in self.due_date.split("-")])

            if self.status == 'finish':
                self.working_status = 'finish'
            elif datetime.date.today() < sdate:
                self.working_status = 'not'
            elif sdate <= datetime.date.today() <= ddate:
                self.working_status = 'in'
            else:
                self.working_status = 'over'

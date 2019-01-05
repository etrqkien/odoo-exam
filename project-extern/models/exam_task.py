# -*- coding: utf-8 -*-

from odoo import fields, models, api


# import datetime


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
        if self.start_date and self.due_date:

            sdate = fields.Datetime.from_string(self.start_date)
            ddate = fields.Datetime.from_string(self.due_date)
            now = fields.Datetime.from_string(fields.Datetime.now())

            if self.status == 'finish':
                self.working_status = 'finish'
            elif now < sdate:
                self.working_status = 'not'
            elif sdate <= now <= ddate:
                self.working_status = 'in'
            else:
                self.working_status = 'over'

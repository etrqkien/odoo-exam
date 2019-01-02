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

    @api.multi
    @api.depends("start_date", "due_date", "status")
    def working_status_compute(self):
        for rec in self:
            if rec.start_date and rec.due_date:

                sdate = fields.Datetime.from_string(rec.start_date)
                ddate = fields.Datetime.from_string(rec.due_date)
                now = fields.Datetime.from_string(fields.Datetime.now())

                if rec.status == 'finish':
                    rec.working_status = 'finish'
                elif now < sdate:
                    rec.working_status = 'not'
                elif sdate <= now <= ddate:
                    rec.working_status = 'in'
                else:
                    rec.working_status = 'over'

            rec.working_status = 'not'

    tag_ids = fields.Many2many('exam.tag', string='Tags')
    priority = fields.Selection(
        [('0', 'Low'), ('1', 'Normal'), ('2', 'High')],
        'Priority', default='1')

    # @api.depends("start_date", "due_date", "status")
    # def working_status_compute(self):
    #     if self.start_date and self.due_date:
    #
    #         sdate = fields.Datetime.from_string(self.start_date)
    #         ddate = fields.Datetime.from_string(self.due_date)
    #         now = fields.Datetime.from_string(fields.Datetime.now())
    #
    #         if self.status == 'finish':
    #             self.working_status = 'finish'
    #         elif now < sdate:
    #             self.working_status = 'not'
    #         elif sdate <= now <= ddate:
    #             self.working_status = 'in'
    #         else:
    #             self.working_status = 'over'
    #
    #     self.working_status = 'not'


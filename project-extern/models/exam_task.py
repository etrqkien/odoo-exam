# -*- coding: utf-8 -*-

from odoo import fields, models, api


# import datetime


class ExamTask(models.Model):
    _inherit = 'exam.task'
    _order = 'priority desc, due_date asc'
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
        [('0', 'Low'), ('1', 'Normal'), ('2', 'High'), ('3', 'Extremely High')],
        'Priority', default='1')

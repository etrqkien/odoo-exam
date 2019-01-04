# -*- coding: utf-8 -*-

from odoo import fields, models, api
import datetime


class Task(models.Model):
    _name = 'exam.task'
    _description = 'My task'

    name = fields.Char("Ten task")
    user_id = fields.Many2one('res.users', string="Id User")
    start_date = fields.Date("Ngay bat dau")
    due_date = fields.Date("Ngay ket thuc")
    project_id = fields.Many2one('exam.project', string="ID project")
    status = fields.Selection(
        [('init', 'Init'), ('finish', 'Finish'), ('fail', 'Fail')], "Trạng thái")
    compute = fields.Selection(
        [('chuabd', 'Not start'), ('danghoatdong', 'In Working time'), ('dakt', 'Finish'), ('quahan', 'Over Deadline')],
        "Working_status")

    @api.onchange("start_date", "due_date", "status")
    def _amount_onchange(self):

        dt = datetime.datetime.now()
        dt_current = dt.strftime("%Y-%m-%d")
        if self.status == 'finish':
            self.compute = 'dakt'
        elif str(self.start_date) > dt_current:
            self.compute = 'chuabd'
        elif str(self.start_date) < dt_current < str(self.due_date):
            self.compute = 'danghoatdong'
        else:
            self.compute = 'quahan'

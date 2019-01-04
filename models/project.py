# -*- coding: utf-8 -*-

from odoo import fields, models, api
import datetime


class Project(models.Model):
    _name = 'exam.project'
    _description = 'My project'

    name = fields.Char("Ten du an")
    manager_user_id = fields.Char("Id User Quan ly")
    start_date = fields.Date("Ngay bat dau")
    due_date = fields.Date("Ngay ket thuc")
    task_ids = fields.Many2one('exam.task', string="Danh sach task")
    status = fields.Selection(
        [('init', 'Init'), ('finish', 'Finish'), ('fail', 'Fail')], "Trang thai", default='init')
    compute = fields.Selection(
        [('chuabatdau', 'Chua bat dau'), ('danghoatdong', 'Dang hoat dong'), ('dakt', 'Da ket thuc')],
        "Trang thai hoat dong")

    @api.onchange("start_date", "due_date")
    def _amount_onchange(self):

        dt = datetime.datetime.now()
        dt_current = dt.strftime("%Y-%m-%d")
        if str(self.start_date) > dt_current:
            self.compute = 'chuabatdau'
        elif str(self.start_date) < dt_current < str(self.due_date):
            self.compute = 'danghoatdong'
        else:
            self.compute = 'dakt'

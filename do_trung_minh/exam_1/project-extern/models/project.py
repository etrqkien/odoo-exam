# -*- coding: utf-8 -*-
from odoo import models, fields, api
import datetime


class ProjectIntern(models.Model):
    _inherit = 'iuh.project'

    status = fields.Selection(selection=[
        ('1', 'init'),
        ('2', 'finish'),
        ('3', 'fail')],
        default='1', string="Trạng thái")

    working_status = fields.Selection(selection=[
        ('1', 'Chưa bắt đầu'),
        ('2', 'Đang hoạt động'),
        ('3', 'Đã kết thúc')],
        compute="_working_status",string="Hoạt động")

    @api.depends('start_date', 'due_date')
    def _working_status(self):
        for self1 in self:
            self1.ensure_one()
            start_date = fields.Datetime.from_string(self1.start_date)
            end_date = fields.Datetime.from_string(self1.due_date)
            current_date = datetime.datetime.today()
            if start_date > current_date:
                self1.working_status = "1"
            elif start_date < current_date < end_date:
                self1.working_status = "2"
            else:
                self1.working_status = "3"

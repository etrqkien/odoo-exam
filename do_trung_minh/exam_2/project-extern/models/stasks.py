# -*- coding: utf-8 -*-
from odoo import models, fields, api
import datetime


class TasksIntern(models.Model):
    _inherit = 'iuh.tasks'

    status = fields.Selection(selection=[
        ('1', 'init'),
        ('2', 'in progress'),
        ('3', 'finish ')],
        default='1', string="Trạng thái")

    working_status = fields.Selection(selection=[
        ('1', 'not start'),
        ('2', 'in working time'),
        ('3', 'finish'),
        ('4', 'over dead line')],
        compute="_working_status", default='1',
        string="Hoạt động")
    tags_id = fields.Many2many('exam.tag', string="Tags")
    priority = fields.Selection(
        [('0', 'Low'),
         ('1', 'Normal'),
         ('2', 'High')],
        'Priority', default='1')

    @api.multi
    @api.depends('start_date', 'due_date', 'status')
    def _working_status(self):
        for self1 in self:
            self1.ensure_one()
            start_date = fields.Datetime.from_string(self1.start_date)
            end_date = fields.Datetime.from_string(self1.due_date)
            current_date = datetime.datetime.today()
            if self1.status == '3':
                self1.working_status = "3"
            else:
                if start_date > current_date:
                    self1.working_status = "1"
                elif start_date < current_date < end_date:
                    self1.working_status = "2"
                else:
                    self1.working_status = "4"

    @api.multi
    def _reopen_form(self):
        self.ensure_one()

        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,  # this model
            'res_id': self.id,  # the current wizard record
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new'}
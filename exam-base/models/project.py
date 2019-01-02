# -*- coding: utf-8 -*-
from odoo import fields, models, api, exceptions


class Project (models.Model):
    _name = 'exam.project'
    name = fields.Char(string='Name Project')
    manager_user_id = fields.Char()
    start_date = fields.Date()
    due_date = fields.Date()
    task_ids = fields.One2many(
        string=u'Danh sach cac Task',
        comodel_name='exam.task',
    )
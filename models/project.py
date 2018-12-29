# -*- coding: utf-8 -*-
from odoo import fields, models, api


class Project (models.Model):
    _name = 'exam.project'
    name = fields.Char('Name Project')
    manager_user_id = fields.Char()
    start_date = fields.Datetime()
    due_date = fields.Datetime()
    task_ids = fields.Char()
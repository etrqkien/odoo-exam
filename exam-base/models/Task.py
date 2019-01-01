# -*- coding: utf-8 -*-
from odoo import fields, models, api


class Task (models.Model):
    _name = 'exam.task'
    name = fields.Char(string="Name task")
    user_id = fields.Many2one('res.users')
    start_date = fields.Datetime()
    due_date = fields.Datetime()
    project_id=fields.Many2one("exam.project")
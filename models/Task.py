# -*- coding: utf-8 -*-
from odoo import fields, models, api


class Task (models.Model):
    _name = 'exam.task'
    user_id = fields.Many2one('res.users','Nguoi thuc hien')
    start_date = fields.Datetime()
    due_date = fields.Datetime()
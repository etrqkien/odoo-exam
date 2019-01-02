# -*- coding: utf-8 -*-
from odoo import fields, models, api


class Task (models.Model):
    _name = 'exam.task'
    name = fields.Char(string="Name task")
    user_id = fields.Many2one(comodel_name='res.users',
                              string='nguoi thuc hien',
                              )
    start_date = fields.Date()
    due_date = fields.Date()
    project_id = fields.Many2one(comodel_name="exam.project",
                                 string=u'Project',
                                 )

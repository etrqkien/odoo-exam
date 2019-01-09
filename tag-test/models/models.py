# -*- coding: utf-8 -*-

from odoo import models, fields


class Tags(models.Model):
    _name = "exam.tags"
    _description = "Tags"
    name = fields.Char("Name_Tag")
    task_ids = fields.Many2many('exam.tasks', required=True)


class Tasks(models.Model):
    _name = "exam.tasks"
    _description = "Tasks"
    name = fields.Char("Name_Task")
    user_id = fields.Many2one("res.users", required=True)
    tag_ids = fields.Many2many('exam.tags', required=True)
    priority = fields.Integer()

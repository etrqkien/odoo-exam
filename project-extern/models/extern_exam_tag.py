# -*- coding: utf8 -*-
from odoo import fields, models

class ExtExamTag(models.Model):
    _name = "exam.tag"

    name = fields.Char("Tag Name")

    tag_ids = fields.Many2many("exam.task", "exam_task_tag_rel")
# -*- coding: utf-8 -*-
from odoo import models, fields


class ExamTag(models.Model):
    _name = 'exam.tag'
    _description = 'Tag'

    name = fields.Char('Name')

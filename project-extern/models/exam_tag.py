# -*- coding: utf-8 -*-
from odoo import models, fields


class ExamTag(models.Model):
    _name = 'exam.tag'
    _description = 'Tag'
    _order = 'name asc'

    name = fields.Char('Name')

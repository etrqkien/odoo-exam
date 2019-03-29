from odoo import models, fields, api
import datetime


class Tags(models.Model):
    _name = 'exam.tag'

    name = fields.Char(string="Thẻ")

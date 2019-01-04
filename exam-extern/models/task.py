# -*- coding: utf-8 -*-
from odoo import models, fields, api
import datetime

class Task(models.Model):
    _inherit = 'exam.task'
    status = fields.Selection([('init', 'khoi tao'), ('inprogess', 'dang lam viec'), ('finish', 'kethuc')])
    working_status = fields.Selection(
        [('bd', 'not start'), ('dang', 'in working time'), ('kt', 'finish'), ('qua han', 'over deadline')],
        compute='caculate_date')

    @api.onchange('status', 'working_status')
    def caculate_date(self):

        if (self.status == 'init'):
            self.working_status = 'bd'

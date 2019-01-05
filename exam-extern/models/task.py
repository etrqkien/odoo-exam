# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Task(models.Model):
    _inherit = 'exam.task'
    status = fields.Selection(selection=[('init', 'khoi tao'), ('inprogess', 'dang lam viec'), ('finish', 'kethuc')])
    working_status = fields.Selection(
        selection=[('bd', 'not start'), ('dang', 'in working time'), ('kt', 'finish'), ('quahan', 'over deadline')],
        compute='working_status_compute'
    )
    @api.onchange('status','working_status')
    def working_status_compute(self):
        if self.start_date and self.due_date:

            sdate = fields.Date.from_string(self.start_date)
            ddate = fields.Date.from_string(self.due_date)
            today = fields.Date.from_string(fields.Date.today())

            if self.status == 'finish':
                self.working_status = 'kt'
            elif today < sdate:
                self.working_status = 'bd'
            elif sdate <= today <= ddate:
                self.working_status = 'dang'
            else:
                self.working_status = 'quahan'
# -*- coding: utf8 -*-
from odoo import fields, models, api

class ExtExamTask(models.Model):
    _inherit = "exam.task"
    _order = "priority desc"

    status = fields.Selection([("1", "init"),
                               ("2", "inprogress"),
                               ("3", "finish")], "Status")
    working_status = fields.Selection([("1", "Not start"),
                                       ("2", "In working time"),
                                       ("3", "Finish"),
                                       ("4", "Over date line")], "Working Status", compute="_compute_wk_status")

    tag_ids = fields.Many2many("exam.tag", string="Tags")
    priority = fields.Selection([('1', 'Low'),
                                 ('2', 'Normal'),
                                 ('3', 'High'),
                                 ('4', 'Very High')],
                                'Priority', default='1')
    user_id = fields.Many2one("res.users", "User")

    @api.multi
    @api.depends("status", "start_date", "due_date")
    def _compute_wk_status(self):
        day_now = fields.Date.from_string(fields.Date.today())

        for item in self:
            if item.start_date and item.due_date:
                start_date2str = fields.Date.from_string(item.start_date)
                due_date2str = fields.Date.from_string(item.due_date)

                if item.status == "3":
                    item.working_status = "3"
                elif day_now < start_date2str:
                    item.working_status = "1"
                elif day_now < due_date2str and day_now > start_date2str:
                    item.working_status = "2"
                elif due_date2str < day_now:
                    item.working_status = "4"



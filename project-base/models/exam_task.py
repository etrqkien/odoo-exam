from odoo import models, fields


class Exam_task(models.Model):
    _name = "exam.task"
    name = fields.Char("ten task")
    user_id = fields.Many2one(comodel_name="res.users", string="quan ly task",)
    start_date = fields.Date("ngayf bat dau")
    due_date = fields.Date("ngay ket thuc")
    project_id = fields.Many2one(comodel_name="exam.project", string="quan ly task trong project",)

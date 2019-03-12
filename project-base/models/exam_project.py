from odoo import models, fields


class Exam_project(models.Model):
    _name = "exam.project"
    name = fields.Text("ten project")
    manager_user_id = fields.Many2one(comodel_name="res.users", string="quan ly project", required=False, )
    start_date = fields.Date("ngay bat dau")
    due_date = fields.Date("ngay ket thuc")
    task_id = fields.One2many(comodel_name="exam.task",
                              inverse_name="project_id",
                              string="quan ly task",
                              required=False,)

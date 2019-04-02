from odoo import models, fields
class Exam_tag(models.Model):
    _name = "exam.tag"
    name = fields.Char("ten tag")
    tag_ids = fields.Many2many(comodel_name="exam.task", string="tag cua task",)



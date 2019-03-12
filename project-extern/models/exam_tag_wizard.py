# -*- coding: utf8 -*-
from odoo import fields, models
import re

class WizardTag(models.TransientModel):
    _name = "wizard.tag"

    w_task = fields.Many2one("exam.task", "Task")
    w_tag = fields.Char("Tags")
    w_u_option = fields.Selection([("add", "Add"),
                                   ("rep", "Replace"),
                                   ("del", "Delete")], "Update Option", default="add")

    def wizard_update(self):
        tags = re.split(r'\.|\,|\-|\_', self.w_tag)
        
        rec_wizard_tag = self.env["exam.tag"]
        rec_task_tab = [i.name for i in rec_wizard_tag.search([])]
        exam_task_tab = [name for name in tags if name not in rec_task_tab]

        for name in exam_task_tab:
            rec_wizard_tag.create({"name": name})

        id_tag = [i.id for i in rec_wizard_tag.search([]) if i.name in tags]

        if self.w_u_option == "add":
            for id in id_tag:
                self.w_task.write({"tag_ids": [([4, id])]})

        elif self.w_u_option == "rep":
            self.w_task.write({"tag_ids": [([6, 0, id_tag])]})

        elif self.w_u_option == "del":
            for id in id_tag:
                self.w_task.write({"tag_ids": [([3, id])]})
            pass


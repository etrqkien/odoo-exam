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

    def _reopen_form(self):
        '''Reload exam task after update'''
        
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'exam.task',
            # 'res_id': self.id,
            # 'view_type': 'form',
            'view_mode': 'kanban,tree,form',
            'target': 'current',
            'name': 'Exam Tag Action'
        }

    def wizard_update(self):
    	# Split Tags fields to Tags
        tags = [x.strip() for x in re.split(r'\.|\,|\-|\_', self.w_tag)]

        # Get exam_tag model 
        rec_wizard_tag = self.env["exam.tag"]

        # Get all field name of exam_tag
        rec_task_tab = [i.name for i in rec_wizard_tag.search([])]

        # Get all Tag name in tags not in rec_task_tab
        exam_task_tab = [name for name in tags if name not in rec_task_tab]

        # add tag not exist to exam_tag table
        for name in exam_task_tab:
            rec_wizard_tag.create({"name": name})

        # Get all id of tag value on tags after insert to databse
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

        return self._reopen_form()


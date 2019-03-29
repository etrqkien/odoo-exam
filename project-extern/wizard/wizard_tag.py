from odoo import models, fields, api


class wizard_tag(models.TransientModel):
    _name = "wizard.tag"
    Task_id = fields.Many2one(comodel_name="exam.task", string="task")
    Tags = fields.Char("tags")
    Update_option = fields.Selection(string="", selection=[('add', 'Add'),
                                                           ('replace', 'Replace'),
                                                           ('delete', 'Delete'), ], default="add")

    def reload(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'exam.task',
            'view_mode': 'kanban,tree,form',
            'name': 'task view'
        }

    def tag_update(self):
        name_rec_tag = []
        tag_list_id = []
        tag_list = self.Tags.split(',')
        rec_tag = self.env['exam.tag']
        for i in rec_tag.search([]):
            name_rec_tag.append(i.name)
            if i.name in tag_list:
                tag_list_id.append(i.id)
        for tag in tag_list:
            if tag not in name_rec_tag:
                rec_tag.create({"name": tag})

        if self.Update_option == "add":
            for id in tag_list_id:
                self.Task_id.write({
                    "tag_ids": [([4, id])]
                })
        elif self.Update_option == "replace":
            self.Task_id.write({"tag_ids": [([6, 0, tag_list_id])]})

        elif self.Update_option == "delete":
            for id in tag_list_id:
                self.Task_id.write({"tag_ids": [([3, id])]})

        return self.reload()

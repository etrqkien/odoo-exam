from odoo import models, fields, api


class Wizard(models.TransientModel):
    _name = "iuh.wizard"

    task_id = fields.Many2one('iuh.tasks', string="Task")
    tag_ids = fields.Char(string="Tags")
    option = fields.Selection([('add', 'Add'), ('delete', 'Delete'), ('replace', 'Replace')], default="add")

    @api.multi
    def button_save(self):
        for record in self:

            if record.tag_ids:
                tags = []
                tags2 = []

                for a in record.tag_ids.split(','):
                    if record.env['exam.tag'].search_count([('name', '=', a)]) == 0:
                        tag = record.env['exam.tag'].create({'name': a})
                        tags.append(tag.id)
                    else:
                        tag2 = record.env['exam.tag'].search([('name', '=', a)])
                        tags2.append(tag2.id)

                # self.task_id.tags_id = tags
                ts = self.env['iuh.tasks'].browse(self.task_id.id)
                if self.option == "add":
                    ts.tags_id = tags

                elif self.option == "delete":
                    ts.tags_id = [(5, self.task_id.id, tags2)]

                else:
                    ts.tags_id = [(6, self.task_id.id, tags)]
                    ts.tags_id = [(6, self.task_id.id, tags2)]

        return True

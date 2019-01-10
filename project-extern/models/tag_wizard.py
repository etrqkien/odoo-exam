#	-*-	coding:	utf-8	-*
from odoo import models, fields, api, exceptions
import logging

_logger = logging.getLogger(__name__)


class TagWizard(models.TransientModel):
    _name = 'tag.wizard'
    _description = 'Tag Wizard'

    task_id = fields.Many2one('exam.task', string='Task')
    tags = fields.Char('Tags')

    update_option = fields.Selection(
        [('add', 'Add'), ('replace', 'Replace'), ('delete', 'Delete')],
        'Update Option', required=True, default='add',
    )

    @api.multi
    def tag_update(self):
        self.ensure_one()
        # if not (self.task_id or self.tags):
        #     raise exceptions.ValidationError('No data to update!')
        # _logger.debug('Update on %s', self.task_id.ids)
        if self.tags:
            tag_list = self.tags.split(',')
            if self.update_option == 'add':

                for tag in tag_list:
                    tag = tag.strip()
                    if self.env['exam.tag'].search([('name', '=', tag)]):
                        tag_add = self.env['exam.tag'].search([('name', '=', tag)])
                    else:
                        tag_add = self.env['exam.tag'].create({'name': tag})

                    self.task_id.write({'tag_ids': [(4, tag_add.id)]})

            elif self.update_option == 'replace':

                tag_add_list = []
                for tag in tag_list:
                    tag = tag.strip()
                    if self.env['exam.tag'].search([('name', '=', tag)]):
                        tag_add = self.env['exam.tag'].search([('name', '=', tag)])
                    else:
                        tag_add = self.env['exam.tag'].create({'name': tag})
                    tag_add_list.append(tag_add.id)

                self.task_id.write({'tag_ids': [(6, 0, tag_add_list)]})

            else:
                for tag in tag_list:
                    tag = tag.strip()
                    if self.env['exam.tag'].search([('name', '=', tag)]):
                        tag_add = self.env['exam.tag'].search([('name', '=', tag)])
                        self.task_id.write({'tag_ids': [(3, tag_add.id)]})

        return True

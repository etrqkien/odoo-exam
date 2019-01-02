#	-*-	coding:	utf-8	-*
from odoo import models, fields, api, exceptions
import logging

_logger = logging.getLogger(__name__)


class TagWizard(models.TransientModel):
    _name = 'tag.wizard'
    _description = 'Tag Wizard'

    task_id = fields.Many2one('exam.task', string='Task')
    tags_relate = fields.Many2one('exam.tag')
    tags = fields.Char('Tags')

    update_option = fields.Selection(
        [('add', 'Add'), ('replace', 'Replace'), ('delete', 'Delete')],
        'Update Option', default='add'
    )

    @api.multi
    def tag_update(self):
        self.ensure_one()
        if not (self.task_id or self.tags):
            raise exceptions.ValidationError('No data to update!')
        _logger.debug('Update on %s', self.task_id.ids)

        vals = {}
        if self.task_id:
            vals['name'] = self.task_id['name']
        if self.tags:
            tag_list = self.tags.split(',')
            val_tag = {}
            for tag in tag_list:
                val_tag['name'] = tag
                for tag_name in self.tags_relate:
                    # Thêm tag mới
                    if tag_name != tag:
                        if val_tag:
                            self.tags_relate.create(val_tag)
            vals['tag_ids'] = tag_list
        # Update task
        if vals:
            self.task_id.write(vals)

        return True

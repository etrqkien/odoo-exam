# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class Tags(models.Model):
    _name = "test.tags"
    _description = "this is tags"
    name = fields.Char("Name Tag")
    task_ids = fields.Many2many('test.tasks', required=True)


class Tasks(models.Model):
    _name = "test.tasks"
    _description = "this is tasks"
    name = fields.Char("Name Task")
    user_id = fields.Many2one("res.users", required=True)
    tag_ids = fields.Many2many('test.tags', required=True)
    priority = fields.Selection(
        [('0', 'Low'), ('1', 'Normal'), ('2', 'High'), ('3', 'So High')],
        'Priority', default='3')


class Wizard(models.Model):
    _name = 'tags.wizard'
    task_ids = fields.Many2one("test.tasks")
    tag_ids = fields.Char()
    option = fields.Selection([('add', 'Add'), ('replace', 'replace'), ('delete', 'delete')], "Update option",
                              default='add')

    @api.multi
    def action_update(self):
        self.ensure_one()
        if(self.task_ids == False | self.tag_ids==False):
            raise exceptions.ValidationError("khong co du lieu ")
        return True

        task = self.env['test.tasks']

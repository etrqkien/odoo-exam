# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class Stage(models.Model):
    _name = "test.stage"
    name = fields.Char("Name Stage")


class Tags(models.Model):
    _name = "test.tags"
    _description = "this is tags"
    name = fields.Char("Name Tag")
    task_ids = fields.Many2many('test.tasks')


class Tasks(models.Model):
    _name = "test.tasks"
    _order = 'priority desc'
    _description = "this is tasks"
    name = fields.Char("Name Task")
    stage_id = fields.Many2one("test.stage")
    user_id = fields.Many2one("res.users", required=True)
    tag_ids = fields.Many2many('test.tags', required=True)
    priority = fields.Selection(
        [('0', 'Low'), ('1', 'Normal'), ('2', 'High'), ('3', 'So High')],
        'Priority', default='3')


class Wizard(models.TransientModel):
    _name = 'tags.wizard'
    task_ids = fields.Many2one("test.tasks", required=True)
    tag_ids = fields.Char(required=True)
    option = fields.Selection([('add', 'Add'), ('replace', 'replace'), ('delete', 'delete')], "Update option",
                              default='add')

    @api.multi
    def action_update(self):
        self.ensure_one()
        if self.option == 'add':
            MyTags = self.env['test.tags'].search([])
            tags = self.tag_ids.split(",")
            for tag in tags:
                for tag_name in MyTags:
                    if tag_name.name == tag:
                        break
                MyTags.create({'name': tag})
            return True
        # if self.option == 'replace':
        #
        # if self.option == 'delete':

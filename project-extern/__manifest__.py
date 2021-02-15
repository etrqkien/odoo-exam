# -*- coding: utf8 -*-
{
    "name": "Project Base External",
    "description": "Bai test ve ke thua trong odoo",
    "author": "Dao Duy Huy",
    "depends": ["project-base"],
    "data": ["security/ir.model.access.csv" ,
             "views/ex_exam_project.xml",
             "views/ex_exam_task.xml",
             "views/exam_tag.xml",
             "views/exam_tag_wizard.xml"],
    "application": True,

}
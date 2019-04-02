from odoo import models, fields,api

class task_extern(models.Model):
    _inherit = "exam.task"
    _order = "priority desc"

    tag_ids = fields.Many2many(comodel_name="exam.tag", string="tag_id", )
    priority = fields.Selection([('1', 'Low'),
                                 ('2', 'Normal'),
                                 ('3', 'High'),
                                 ('4', 'Very High')],
                                'Priority', )

    status = fields.Selection(string="trang thai", selection=[('init', 'init'),
                                                    ('inprogress', 'inprogress'),
                                                    ('finish', 'finish'), ],
                              required=False, )
    compute_working_status = fields.Selection(string="tinh trang task", selection=[('not', 'not start'),
                                                                    ('in', 'in working time'),
                                                                    ('finish', 'finish'),
                                                                    ('over', 'over dead line'), ],
                                              required=False,
                                              compute="cpt_compute_working_status", )
    @api.multi
    @api.depends('start_date','due_date','status')
    def cpt_compute_working_status(self):
        for rec in self:
            if rec.start_date and rec.due_date:
                sdate = fields.Date.from_string(rec.start_date)
                ddate = fields.Date.from_string(rec.due_date)
                today = fields.Date.from_string(fields.Date.today())
                if rec.status=='finish':
                    rec.compute_working_status='finish'
                elif today < sdate:
                    rec.compute_working_status = 'not'
                elif sdate <= today <= ddate:
                    rec.compute_working_status = 'in'
                else:
                    rec.compute_working_status = 'over'

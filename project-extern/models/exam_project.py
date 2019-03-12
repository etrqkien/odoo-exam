from odoo import models, fields, api


class project_extern(models.Model):
    _inherit = "exam.project"
    status = fields.Selection(string="trang thai",
                              selection=[('init', 'Init'),
                                         ('finish', 'Finish'),
                                         ('fail', 'Fail'), ],
                              default='init',
                              )
    working_status = fields.Selection(string="trang thai thuc hien ", selection=[('chua', 'chua bat dau'),
                                                                                  ('dang', 'dang hoat dong'),
                                                                                  ('da', 'da ket thuc'), ],
                                      required=False, compute="cpt_working_status")

    @api.multi
    @api.depends('start_date', 'due_date')
    def cpt_working_status(self):
        for rec in self:
            if rec.start_date and rec.due_date:

                sdate = fields.Date.from_string(rec.start_date)
                ddate = fields.Date.from_string(rec.due_date)
                today = fields.Date.from_string(fields.Date.today())

                if today < sdate:
                    rec.working_status = 'chua'
                elif sdate <= today <= ddate:
                    rec.working_status = 'dang'
                else:
                    rec.working_status = 'da'

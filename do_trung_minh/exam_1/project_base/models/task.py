from odoo import models, fields, api


class IuhTask(models.Model):
    _name = 'iuh.tasks'
    _description = u'Quản lý Trường Đại học Công nghiệp TPHCM (IUH)'

    user_id = fields.Many2one('res.users', string='Người Thực hiện')
    start_date = fields.Datetime(string="Ngày bắt đàu task", default=lambda self: fields.datetime.now())
    name = fields.Char(string='Tên task', required=True)
    due_date = fields.Datetime(u"Ngày kết thúc task", default=lambda self: fields.datetime.now())
    project_id = fields.Many2one(comodel_name='iuh.project', string='Tên dự án', store=True)

    # @api.multi
    # def some_fuction(self):
    #     # This will make sure we have on record, not multiple records.
    #     self.ensure_one()
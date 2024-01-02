from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import datetime, timedelta

class Task(models.Model):
    _name = 'task_manager.task'
    _description = 'Task Management'

    
    state = fields.Selection([
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ], string='Status', default='in_progress')
    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    deadline = fields.Date(string='Deadline')
    days_left = fields.Integer(string='Days Left', compute='_compute_days_left', store=True)

    @api.depends('deadline')
    def _compute_days_left(self):
        for task in self:
            if task.deadline:
                deadline_date = fields.Date.from_string(task.deadline)
                today_date = fields.Date.from_string(fields.Date.today())
                days_left = (deadline_date - today_date).days
                task.days_left = max(0, days_left)

    def mark_as_completed(self):
        self.write({'state': 'completed'})

    def print_all_tasks_report(self):
        return self.env.ref('task_manager.task_report').report_action(self)
    
    def get_all_tasks(self):
        return self.env['task_manager.task'].search([])




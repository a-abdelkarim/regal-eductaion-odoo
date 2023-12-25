from odoo import models, fields


class Visit(models.Model):
    _name = 'visit'
    _description = 'School Visit'
    
    name = fields.Char('name')
    notes = fields.Text('notes')
    date = fields.Datetime('date')
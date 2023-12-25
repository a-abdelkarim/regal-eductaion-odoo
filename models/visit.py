from odoo import models, fields


class Visit(models.Model):
    _name = 'visit'
    _description = 'School Visit'
    
    name = fields.Char('name')
    partner_id = fields.Many2one(comodel_name='res.partner', string='Customer', required=True)
    notes = fields.Text('notes')
    date = fields.Datetime('date')
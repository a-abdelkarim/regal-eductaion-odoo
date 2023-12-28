from odoo import api, models, fields


class Visit(models.Model):
    _name = 'visit'
    _description = 'School Visit'
    
    name = fields.Char('name')
    partner_id = fields.Many2one(comodel_name='res.partner', string='Customer', required=True)
    partner_name = fields.Char(related='partner_id.name')
    school_curriculum = fields.Selection(related='partner_id.curriculum_type')
    school_state = fields.Many2one(related='partner_id.state_id')
    school_email = fields.Char(related='partner_id.email')
    notes = fields.Text('notes')
    date = fields.Datetime('date')
    
    create_uid = fields.Many2one('res.users', 'Created By', default=lambda self: self.env.uid, readonly=True)

    @api.model
    def create(self, values):
        # get partner
        partner = self.env['res.partner'].sudo().browse([values.get("partner_id")])

        values['create_uid'] = self.env.uid
        values['name'] = f'{partner.name} - {values.get("date")}'
        return super(Visit, self).create(values)
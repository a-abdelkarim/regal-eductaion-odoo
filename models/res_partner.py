from odoo import models, fields


CURRICULUM_TYPES = [
    ('american', "American"),
    ('british', "British"),
]

class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'Partner Inherit'

    manager_name = fields.Char(string="Manager Name")
    manager_phone = fields.Char(string="Manager Phone")
    responsible_name = fields.Char(string="Responsible Name")
    responsible_phone = fields.Char(string="Responsible Phone")
    curriculum_type = fields.Selection(selection=CURRICULUM_TYPES, default='american')
    
    latitude = fields.Float()
    longitude = fields.Float()
    
    
    
    def view_school_location(self):
        return {
            'type': 'ir.actions.act_url',
            # 'url': f'https://www.google.com/maps/place/{self.latitude},{self.longitude},13z?entry=ttu',
            'url': f'https://www.google.com.sa/maps/search/{self.latitude},{self.longitude}',
            'target': 'new',
        }
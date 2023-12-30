from odoo import models, fields


CURRICULUM_TYPES = [
    ('american', "American"),
    ('british', "British"),
    ('multiple', 'Multiple')
]


PRIMARY_CURRICULUMS = [
    ('american', 'American'),
    ('british', 'British'),
]


SCHOOL_TYPES = [
    ('actual', 'Actual Customer'),
    ('potential', 'Potential Customer'),
    ('followed', 'Followed Customer'),
]


class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'School'

    arabic_name = fields.Char("Arabic Name")
    manager_name = fields.Char(string="Manager Name")
    manager_phone = fields.Char(string="Manager Phone")
    manager_email = fields.Char(string="Manager Email")
    academic_name = fields.Char(string="Academic Name")
    academic_phone = fields.Char(string="Academic Phone")
    academic_email = fields.Char(string="Academic Email")
    curriculum_type = fields.Selection(selection=CURRICULUM_TYPES, default='american')
    primary_curriculum = fields.Selection(selection=PRIMARY_CURRICULUMS, default='american')
    school_type = fields.Selection(selection=SCHOOL_TYPES, default='actual')
    location_link = fields.Char("Location Link") 
    latitude = fields.Float()
    longitude = fields.Float()
    visits_history_ids = fields.One2many(
        comodel_name="visit", inverse_name="partner_id", string="Visits History", required=False
    )
    
    
    def view_school_location(self):
        return {
            'type': 'ir.actions.act_url',
            # 'url': f'https://www.google.com/maps/place/{self.latitude},{self.longitude},13z?entry=ttu',
            'url': f'https://www.google.com.sa/maps/search/{self.latitude},{self.longitude}',
            'target': 'new',
        }
        
    def view_school_location_with_link(self):
        if self.location_link:
            return {
                'type': 'ir.actions.act_url',
                'url': self.location_link,
                'target': 'new',
            }
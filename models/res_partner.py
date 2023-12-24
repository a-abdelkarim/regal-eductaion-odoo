from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'Partner Inherit'

    manager_name = fields.Char(string="Manager Name")
    manager_phone = fields.Char(string="Manager Phone")
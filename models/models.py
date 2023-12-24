# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class arab/regal_education(models.Model):
#     _name = 'arab/regal_education.arab/regal_education'
#     _description = 'arab/regal_education.arab/regal_education'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

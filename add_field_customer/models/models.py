	# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class jme_custom(models.Model):
#     _name = 'jme_custom.jme_custom'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()

#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class JmeCustom(models.Model):
	_inherit = 'product.template'

	customer_specific_id = fields.Many2one('res.partner',
    	string='Customer',
    	domain=[('customer', '=', True)],
   		help='Fill this in if this product is specific to a certain customer',
    )

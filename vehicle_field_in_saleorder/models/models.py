# -*- coding: utf-8 -*-

from odoo import models, fields, api

class jme_vehicle_field_in_saleorder(models.Model):
	_inherit = 'sale.order'

	vehicle_list = fields.Many2one('fleet.vehicle',
    	#domain=[('customer_specific_id', 'in', partner_id.id)],
    	string='Vehicle',
    	help='Only show vehicles belong to selected customer'
    	)

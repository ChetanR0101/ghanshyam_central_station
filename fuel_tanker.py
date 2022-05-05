from odoo import models, fields

class FuelTanker(models.Model):
    _name = 'fuel.tanker'

    regitration_no = fields.Char(string="Tanker registration Number")
    description = fields.Char(string='Record Description')
    fuel_categ = fields.Many2one(comodel_name="fuel.category")
    source = fields.Char(string="Tanker Source")
    destination = fields.Char(string="Tanker Destination")
    capacity = fields.Float(string="Storage Capacity")
    # carried_volume = fields.Float(string="Fuel Carried")
    
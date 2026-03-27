# A sample of the custom logic structure used in the Capstone project
# Demonstrates inheriting from Odoo's 'sale.order' model to add custom fields

from odoo import models, fields, api

class SaleOrderCustom(models.Model):
    _inherit = 'sale.order'

    # Example of a custom field added during the project
    custom_project_ref = fields.Char(string="Project Reference")
    priority_score = fields.Integer(string="Priority Score", compute="_compute_priority")

    @api.depends('amount_total')
    def _compute_priority(self):
        for record in self:
            # Simple logic sample: High value orders get higher priority
            if record.amount_total > 5000:
                record.priority_score = 10
            else:
                record.priority_score = 5

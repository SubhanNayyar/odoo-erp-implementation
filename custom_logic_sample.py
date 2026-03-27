# Technical Sample: Find My Doctor ERP Customization
# Demonstrates Odoo 14 Module logic for Doctor Management and Security

from odoo import models, fields, api
from odoo.exceptions import UserError

class DoctorProfile(models.Model):
    _name = 'fmd.doctor.profile'
    _description = 'Doctor Panel Management'

    name = fields.Char(string="Doctor Name", required=True)
    specialization = fields.Selection([
        ('gp', 'General Physician'),
        ('cardio', 'Cardiologist'),
        ('pedia', 'Pediatrician')
    ], string="Specialization")
    
    # Logic for specialized dashboard visibility
    is_active = fields.Boolean(default=True)
    consultation_fee = fields.Float(string="Fee")

    @api.model
    def create(self, vals):
        # Security logic sample: Only 'Managers' should be able to create Doctor Profiles
        if not self.env.user.has_group('fmd_erp.group_fmd_manager'):
            raise UserError("Access Denied: Only Managers can add new Doctors to the panel.")
        return super(DoctorProfile, self).create(vals)

# Note: Corresponding XML files defined the Dashboard views for the CEO group

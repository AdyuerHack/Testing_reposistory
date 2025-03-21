from odoo import models, fields, api

class MachineType(models.Model):
    _name = 'machine.type'
    _description = 'Machine Type'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(required=True)
    descripcion = fields.Char(string="Descripción", compute="_compute_descripcion", store=True)
    message_ids = fields.One2many(
        'mail.message', 'res_id', string='Mensajes',
        domain=[('model', '=', 'machine.type')], auto_join=True)
    activity_ids = fields.One2many(
        'mail.activity', 'res_id', string='Activities',
        domain=[('res_model', '=', 'machine.type')]
    )
    
    @api.depends('name')
    def _compute_descripcion(self):
        for record in self:
            record.descripcion = record.name

    def action_print_all(self):
        """Método para imprimir un reporte con todos los registros."""
        machine_types = self.search([])  # Obtiene todos los registros
        return self.env.ref('machine_type_module.action_report_machine_type').report_action(machine_types)
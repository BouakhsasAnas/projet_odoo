from odoo import models, fields

class Absence(models.Model):
    _name = 'gestion.absence'
    _description = 'Absence'

    student_name = fields.Char(string="Nom de l'étudiant", required=True)
    date_absence = fields.Date(string="Date de l'absence", required=True)
    reason = fields.Text(string="Motif de l'absence")

    justified = fields.Boolean(string="Justifiée", default=False)

    justification = fields.Text(string="Justification fournie")
    
    attachment = fields.Binary(string="Pièce justificative (PDF)")
    attachment_name = fields.Char(string="Nom du fichier")

    state = fields.Selection([
        ('absent', 'Absent'),
        ('justifie', 'Justifié')
    ], string="État", default='absent')

from odoo import api, fields, models


class Jalur(models.Model):
    _name = 'pendaftaran.jalur'
    _description = 'Jalur Pendaftaran'

    name = fields.Char(string='Name', required=True)
    deskripsi = fields.Text(string='Deskripsi', required=True)
    kuota = fields.Integer(string='Kuota', required=True)
    biaya = fields.Integer(string='biaya', required=True)

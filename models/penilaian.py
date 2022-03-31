from odoo import api, fields, models


class Penilaian(models.Model):
    _name = 'pendaftaran.penilaian'
    _description = 'Aspek peniliaian calon siswa'

    name = fields.Char(string='Name')
    deskripsi = fields.Text(string='Deskripsi')
    nilai_min = fields.Float(string='Nilai Minimal')

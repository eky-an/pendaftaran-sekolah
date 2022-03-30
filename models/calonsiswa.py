from odoo import api, fields, models


class CalonSiswa(models.Model):
    _name = 'pendaftaran.calonsiswa'
    _description = 'New Description'

    name = fields.Char(string='Name')
    nisn = fields.Char(string='NISN')
    alamat = fields.Text(string='Alamat')
    agama = fields.Selection(string='Agama', selection=[('Islam', 'Islam'), ('Kristen', 'Kristen'), ('Katolik', 'Katolik'), ('Hindu', 'Hindu'), ('Budha', 'Budha'), ('Konghucu', 'Konghucu')])
    jenis_kelamin = fields.Selection(string='Jenis Kelamin', selection=[('Laki-laki', 'Laki-laki'), ('Perempuan', 'Perempuan')])
    tempat_lahir = fields.Char(string='Tempat Lahir')
    tanggal_lahir = fields.Date(string='Tanggal Lahir')
    id_wali = fields.Many2one(comodel_name='pendaftaran.walicalon', string='Wali Calon Siswa')

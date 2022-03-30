from odoo import api, fields, models


class CalonSiswa(models.Model):
    _name = 'pendaftaran.calonsiswa'
    _description = 'New Description'

    name = fields.Char(string='Name')
    nisn = fields.Char(string='NISN')
    alamat = fields.Text(string='Alamat')
    agama = fields.Selection(string='Agama', selection=[('islam', 'Islam'), ('kristen', 'Kristen'), ('katolik', 'Katolik'), ('hindu', 'Hindu'), ('budha', 'Budha'), ('konghucu', 'Konghucu')])
    jenis_kelamin = fields.Selection(string='Jenis Kelamin', selection=[('laki-laki', 'Laki-laki'), ('perempuan', 'Perempuan')])
    tempat_lahir = fields.Char(string='Tempat Lahir')
    tanggal_lahir = fields.Date(string='Tanggal Lahir')

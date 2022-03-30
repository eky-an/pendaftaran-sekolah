from odoo import api, fields, models


class WaliCalon(models.Model):
    _name = 'pendaftaran.walicalon'
    _description = 'New Description'

    name = fields.Char(string='Name')
    nik = fields.Char(string='NIK')
    alamat = fields.Text(string='Alamat')
    status_wali = fields.Selection(string='Status Wali', selection=[('Ayah', 'Ayah'), ('Ibu', 'Ibu'), ('Wali', 'Wali')])
    agama = fields.Selection(string='Agama', selection=[('Islam', 'Islam'), ('Kristen', 'Kristen'), ('Katolik', 'Katolik'), ('Hindu', 'Hindu'), ('Budha', 'Budha'), ('Konghucu', 'Konghucu')])
    jenis_kelamin = fields.Selection(string='Jenis Kelamin', selection=[('Laki-laki', 'Laki-laki'), ('Perempuan', 'Perempuan')])
    pekerjaan = fields.Char(string='Pekerjaan')
    no_hp = fields.Char(string='No HP')

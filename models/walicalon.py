from odoo import api, fields, models


class WaliCalon(models.Model):
    _name = 'pendaftaran.walicalon'
    _description = 'New Description'

    id_calonsiswa = fields.Many2one(comodel_name='pendaftaran.calonsiswa', string='Calon Siswa')
    name = fields.Char(string='Name')
    nik = fields.Char(string='NIK')
    alamat = fields.Text(string='Alamat')
    status_wali = fields.Selection(string='Status Wali', selection=[('ayah', 'Ayah'), ('ibu', 'Ibu'), ('wali', 'Wali')])
    agama = fields.Selection(string='Agama', selection=[('islam', 'Islam'), ('kristen', 'Kristen'), ('katolik', 'Katolik'), ('hindu', 'Hindu'), ('budha', 'Budha'), ('konghucu', 'Konghucu')])
    jenis_kelamin = fields.Selection(string='Jenis Kelamin', selection=[('laki-laki', 'Laki-laki'), ('perempuan', 'Perempuan')])
    pekerjaan = fields.Char(string='Pekerjaan')
    no_hp = fields.Char(string='No HP')

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Daftar(models.Model):
    _name = 'pendaftaran.daftar'
    _description = 'New Description'

    name = fields.Char(string='Kode Pendaftaran', required=True)
    calonsiswa_id = fields.Many2one(comodel_name='pendaftaran.calonsiswa', string='Calon Siswa', required=True)
    jalur_id = fields.Many2one(comodel_name='pendaftaran.jalur', string='Jalur Pendaftaran', required=True)
    tanggal_daftar = fields.Date(string='Tanggal Daftar', required=True)

    biaya_daftar = fields.Integer(string='Biaya Pendaftaran', compute='_compute_biaya_daftar', store=True)

    @api.depends('jalur_id')
    def _compute_biaya_daftar(self):
        administrasi = 100000
        for record in self:
            record.biaya_daftar = record.jalur_id.biaya + administrasi

    @api.model
    def create(self, vals):
        record = super(Daftar, self).create(vals)
        if record.jalur_id:
            self.env['pendaftaran.jalur'].search([('id', '=', record.jalur_id.id)]).write({'kuota':record.jalur_id.kuota - 1})
            return record

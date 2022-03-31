from odoo import api, fields, models


class Kelulusan(models.Model):
    _name = 'pendaftaran.kelulusan'
    _description = 'Kelulusan Calon Siswa'

    name = fields.Char(compute='_compute_name', string='Nama Calon Siswa')
    daftar_id = fields.Many2one(comodel_name='pendaftaran.daftar', string='ID Pendaftaran', required=True)

    @api.depends('daftar_id')
    def _compute_name(self):
        for record in self:
            for record in self:
                record.name = self.env['pendaftaran.calonsiswa'].search([('id', '=', record.daftar_id.calonsiswa_id.id)]).name
    
    
    detailnilai_ids = fields.One2many(comodel_name='pendaftaran.detailpenilaian', inverse_name='kelulusan_id', string='Detail Nilai')
    nilai_akhir = fields.Float(string='Nilai Akhir', compute='_compute_nilai_akhir', store=True)
    
    @api.depends('detailnilai_ids')
    def _compute_nilai_akhir(self):
        nilai = 0.0
        for record in self:
            nilai_akhir = 0.0
            i = 0.0
            for detail in record.detailnilai_ids:
                i += 1
                nilai_akhir += detail.nilai
                nilai = nilai_akhir / i
            record.nilai_akhir = nilai

    lulus = fields.Boolean(string='Lulus', default=False)

    deskripsi = fields.Text(string='Deskripsi', compute='_compute_deskripsi', store=True)

    @api.depends('detailnilai_ids')
    def _compute_deskripsi(self):
        min_rata = 0.0
        for record in self:
            deskripsi = ''
            rata = 0.0
            if record.detailnilai_ids:
                desk = ''
                for detail in record.detailnilai_ids:
                    nama = self.env['pendaftaran.penilaian'].search([('id', '=', detail.penilaian_id.id)]).name
                    min =  self.env['pendaftaran.penilaian'].search([('id', '=', detail.penilaian_id.id)]).nilai_min

                    if detail.nilai < min :
                        desk += nama + ','

                    min_rata += min
                
                rata = min_rata / len(record.detailnilai_ids)

                if record.nilai_akhir >= rata:
                    record.lulus = True
                    deskripsi = 'Lulus'
                else:
                    deskripsi = 'Nilai ' + desk + ' tidak memenuhi syarat'
                    
            record.deskripsi = deskripsi



class DetailPenilaian(models.Model):
    _name = 'pendaftaran.detailpenilaian'
    _description = 'Detail Penilaian Calon Siswa'

    kelulusan_id = fields.Many2one(comodel_name='pendaftaran.kelulusan', string='ID Kelulusan', required=True)
    penilaian_id = fields.Many2one('pendaftaran.penilaian', string='Penilaian')
    nilai = fields.Float(string='Nilai')

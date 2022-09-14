from odoo import api, fields, models


class Jurusan(models.Model):
    _name = 'hogwarts.jurusan'
    _description = 'New Description'

    name = fields.Char(string='Nama Jurusan')
    kode_jurusan = fields.Char(string='Kode Jurusan')

    kelompokmapel_ids = fields.One2many(comodel_name='hogwarts.kelompokmapel', 
                                inverse_name='jurusan_id', 
                                string='Kelompok Mata Pelajaran')

    jml_item = fields.Char(compute='_compute_jml_item', string='Jumlah Kelompok Mata Pelajaran')


    siswa_ids = fields.One2many(comodel_name='hogwarts.siswa', 
                                 inverse_name='jurusan_id', 
                                 string='Daftar Nama Siswa')
    @api.depends('kelompokmapel_ids')
    def _compute_jml_item(self):
        for rec in self:
            a = self.env['hogwarts.kelompokmapel'].search([('jurusan_id','=', rec.id)]).mapped('name')
            b = len(a)
            rec.jml_item = b
            rec.daftar = a
    
    daftar = fields.Char(string='Nama Kelompok Mata Pelajaran')
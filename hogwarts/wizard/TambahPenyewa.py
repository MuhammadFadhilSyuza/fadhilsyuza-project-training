from odoo import api, fields, models

class TambahPenyewa(models.TransientModel):
    _name = 'hogwarts.tambahpenyewa'

    fasilitas_id = fields.Many2one(comodel_name='hogwarts.fasilitas',string='Nama Fasilitas', required=True)
    siswa_id = fields.Many2one(comodel_name='hogwarts.siswa', string='Tambah Siswa')

    def button_tambah_penyewa(self):
        for line in self:
            self.env['hogwarts.fasilitas'].search([('id', '=', line.fasilitas_id.id)]).write(
                {'siswa_id': line.fasilitas_id.siswa_id +  line.siswa_id}
            )
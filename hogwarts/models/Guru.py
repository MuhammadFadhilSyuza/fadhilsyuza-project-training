from odoo import api, fields, models


class Guru(models.Model):
    _name = 'hogwarts.guru'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    ajar = fields.Selection([
    ('fisika','Guru Fisika'), 
    ('kimia','Guru Kimia'),
    ('biologi','Guru Biologi'), 
    ('sosiologi','Guru Sosiologi'),
    ('ekonomi','Guru Ekonomi'), 
    ('Sejarah','Guru Sejarah'),
    ]) 
    id_guru = fields.Char(string='ID Guru')
    tgl_lahir = fields.Date(string='Tanggal Lahir')
    alamat = fields.Char(string='Alamat')
    agama = fields.Char(string='Agama')
    jenis_kelamin = fields.Selection([
    ('laki-laki','Laki Laki'), 
    ('perempuan','Perempuan')
    ]) 
    gol_darah = fields.Selection([
    ('a','A'), 
    ('b','B'),
    ('ab','AB'), 
    ('o','0'),
    ])
    image = fields.Image(string="Image")

    siswa_id = fields.Many2many(comodel_name='hogwarts.siswa', string='Siswa')
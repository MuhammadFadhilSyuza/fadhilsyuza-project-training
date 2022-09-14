from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Siswa(models.Model):
    _name = 'hogwarts.siswa'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    no_induk = fields.Char(string='NISN')
    tgl_lahir = fields.Date(string='Tanggal Lahir')
    alamat = fields.Char(string='Alamat')
    agama = fields.Char(string='Agama')
    jenis_kelamin = fields.Selection([
        ('laki-laki','Laki Laki'), 
        ('perempuan','Perempuan')
    ])
    jurusan = fields.Selection([
        ('ipa','IPA'), 
        ('ips','IPS')
    ])  
    gol_darah = fields.Selection([
        ('a','A'), 
        ('b','B'),
        ('ab','AB'), 
        ('o','O'),
    ])
    image = fields.Image(string="Image")

    nama_ayah = fields.Char(string='Nama Ayah')
    pekerjaan_ayah = fields.Selection([
        ('tidakkerja','Tidak Bekerja'), 
        ('pns','PNS'),
        ('karyaswasta','Karyawan Swasta'), 
        ('petani','Petani'),
        ('lain','Lainnya')
    ])

    nama_ibu = fields.Char(string='Nama Ibu')
    pekerjaan_ibu = fields.Selection([
        ('irt','Ibu Rumah Tangga'), 
        ('pns','PNS'),
        ('karyaswasta','Karyawan Swasta'), 
        ('petani','Petani'),
        ('lain','Lainnya')
    ])

    guru_id = fields.Many2many(comodel_name='hogwarts.guru', string='Guru')
    fasilitas_id = fields.Many2many(comodel_name='hogwarts.fasilitas', string='Fasilitas')
    jurusan_id = fields.Many2one(comodel_name='hogwarts.jurusan', 
                                        string='Nama Jurusan',
                                        ondelete='cascade')

    @api.constrains('alamat')
    def check_alamat(self):
        for rec in self:
            if len(rec.alamat) < 5:
                raise ValidationError("Alamat harus lengkap!")
from odoo import api, fields, models


class KelompokMapel(models.Model):
    _name = 'hogwarts.kelompokmapel'
    _description = 'New Description'

    name = fields.Selection([
        ('mapelipa', 'Mata Pelajaran IPA') , 
        ('mapelips','Mata Pelajaran IPS'),
        ('mapeltambah','Mata Pelajaran Tambahan'),
    ], string='Kelompok Mata Pelajaran')
    kode_mapel = fields.Char(string='Kode Mata Pelajaran')
    
    @api.onchange('name')
    def _onchange_kode_mapel(self):
            if (self.name == 'mapelipa'):
               self.kode_mapel = 'IPA'
            elif (self.name == 'mapelips'):
               self.kode_mapel = 'IPS'
            elif (self.name == 'mapeltambah'):
               self.kode_mapel = 'Tambahan'

    mapel_ids = fields.One2many(comodel_name='hogwarts.mapel', 
                                 inverse_name='kelompokmapel_id', 
                                 string='Daftar Mata Pelajaran')

    jurusan_id = fields.Many2one(comodel_name='hogwarts.jurusan', 
                                        string='Daftar Jurusan',
                                        ondelete='cascade')    

    jml_item = fields.Char(compute='_compute_jml_item', string='Jumlah Mata Pelajaran')

    @api.depends('mapel_ids')
    def _compute_jml_item(self):
        for rec in self:
            a = self.env['hogwarts.mapel'].search([('kelompokmapel_id','=', rec.id)]).mapped('name')
            b = len(a)
            rec.jml_item = b
            rec.daftar = a
    
    daftar = fields.Char(string='List Mata Pelajaran')
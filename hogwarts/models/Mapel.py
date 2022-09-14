from odoo import api, fields, models


class Mapel(models.Model):
    _name = 'hogwarts.mapel'
    _description = 'New Description'

    name = fields.Char(string='Nama Mata Pelajaran')
    kode_mapel = fields.Char(string='Kode Mata Pelajaran')               

    kelompokmapel_id = fields.Many2one(comodel_name='hogwarts.kelompokmapel', 
                                        string='Kelompok Mata Pelajaran',
                                        ondelete='cascade')

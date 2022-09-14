from odoo import api, fields, models


class Fasilitas(models.Model):
    _name = 'hogwarts.fasilitas'
    _description = 'New Description'

    name = fields.Char(string='Nama Fasilitas')
    kode_fasilitas = fields.Char(string='Kode Fasilitas')
    letak_fasilitas = fields.Selection([
        ('lt1','Lantai 1'), 
        ('lt2','Lantai 2'),
        ('lt3','Lantai 3'),
    ]) 

    siswa_id = fields.Many2many(comodel_name='hogwarts.siswa', string='Siswa')
    guru_id = fields.Many2many(comodel_name='hogwarts.guru', string='Guru')


    state = fields.Selection([
            ('draft', 'Draft'),
            ('book', 'Booked'),
            ('done', 'Done'),
            ('cancelled', 'Cancelled'),], 
            string='Room Status', 
            default='draft',
            required=True,
            readonly=True)

    def action_book(self):
        self.write({'state':'book'})

    def action_done(self):
        self.write({'state':'done'})

    def action_cancelled(self):
        self.write({'state':'cancelled'})

    def action_draft(self):
        self.write({'state':'draft'})
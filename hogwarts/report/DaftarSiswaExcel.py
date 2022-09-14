from odoo import models, fields


class PartnerXlsx(models.AbstractModel):
    _name = 'report.hogwarts.report_siswa_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    tgl_laporan = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, siswa):
        # One sheet by partner
        sheet = workbook.add_worksheet('Daftar Siswa')
        # Menambahkan informasi tanggal laporan
        sheet.write(0, 0, str(self.tgl_laporan))
        sheet.write(1, 0, 'Nama Siswa')
        sheet.write(1, 1, 'NISN')
        sheet.write(1, 2, 'Jenis Kelamin')
        sheet.write(1, 3, 'Tanggal Lahir')
        sheet.write(1, 4, 'Jurusan')
        
        row = 2
        col = 0
        for obj in siswa:
            col = 0

            sheet.write(row, col, obj.name)
            sheet.write(row, col + 1, obj.no_induk)
            sheet.write(row, col + 2, obj.jenis_kelamin)
            sheet.write(row, col + 3, str(obj.tgl_lahir))
            for item in obj.jurusan_id:
                sheet.write(row, col + 4, item.name)

            row += 1
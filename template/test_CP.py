import xlsxwriter
import os
import json


class JsonFileXlsx(object):

    def __init__(self, workbook, worksheet):
        self.workbook = xlsxwriter.Workbook('deml.xlsx')
        self.worksheet = self.workbook.add_worksheet('2019_WW13')

        self.cell_format = self.workbook.add_format({
            'bold': True,
            'align': 'center',
            'valign': 'vcenter',
        })

        self.cell_2_format = self.workbook.add_format({
            'bold': True,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
        })

        self.cell_3_format = self.workbook.add_format({
            'bold': True,
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': 'gray',
        })

        self.cell_4_format = self.workbook.add_format({
            'fg_color': 'green',
            'align': 'center',
            'valign': 'vcenter',
            'font_size': 25,
            'border': 1,
        })

        self.cell_5_format = self.workbook.add_format({
            'bg_color': 'green',
            'pattern': True,
            'align': 'center',
            'valign': 'vcenter',
        })

        # 设置宽度
        self.worksheet.set_column('A:A', 18)
        self.worksheet.set_column('B:B', 40)
        self.worksheet.set_column('C:C', 10)
        self.worksheet.set_column('D:D', 20)
        self.worksheet.set_column('E:E', 25)
        self.worksheet.set_column('G:G', 20)
        self.worksheet.set_column('H:H', 15)
        self.worksheet.set_column('I:I', 15)
        self.worksheet.set_column('J:J', 25)
        self.worksheet.set_column('K:K', 10)
        self.worksheet.set_column('L:L', 20)
        self.worksheet.set_column('M:M', 15)
        self.worksheet.set_column('N:N', 15)

    def get_merge_range(self, *args, **kwargs):
        def write_(*args, **kwargs):
            yield self.worksheet.merge_range(*args, **kwargs)

            [item for item in write_(*args, **kwargs)]

    def get_sheet_set_row(self, *args, **kwargs):
        def sheet_(*args, **kwargs):
            yield self.worksheet.set_row(*args, **kwargs)

            [item for item in sheet_(*arge, **kwargs)]

    def run(self):
        self.workbook.close()


if __name__ == '__main__':
    j = JsonFileXlsx('workbook', 'worksheet')
    j.get_merge_range()
    j.get_sheet_set_row()
    j.run()

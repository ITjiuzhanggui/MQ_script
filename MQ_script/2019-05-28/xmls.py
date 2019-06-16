from copy import copy
import xlrd
from xlutils.copy import copy

class XlslSave():
    def __init__(self):
        self.path_name = "2.xlsx"
        self.sheet = "Nginx"

    def append_excel(self, data):
        if type(data[0])== type(list()):
            for item in data:
                book = xlrd.open_workbook(self.path_name, formatting_info=True)
                wfile = copy(book)
                wsheet = wfile.get_sheet(self.sheet)
                wsheet.write(*item)
                wfile.save(self.path_name)
        else:
            book = xlrd.open_workbook(self.path_name)
            wfile = copy(book)
            wsheet = wfile.get_sheet(self.sheet)
            wsheet.write(*data)
            wfile.save(self.path_name)


# data =[[1, 1, '23'],[1, 2, '23']] & data =[1, 1, '23']
# XlslSave().append_excel([[1, 1, '23'],[1, 2, '23']])


# import win32com.client as win32
#
# fname = "2.xls"
# excel = win32.gencache.EnsureDispatch('Excel.Application')
# wb = excel.Workbooks.Open(fname)
#
# wb.SaveAs(fname+"x", FileFormat = 51)    #FileFormat = 51 is for .xlsx extension
# wb.Close()                               #FileFormat = 56 is for .xls extension
# excel.Application.Quit()
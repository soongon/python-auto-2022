import openpyxl
import datetime

wb = openpyxl.workbook.Workbook()

ws = wb.active
ws['A1'] = 'Hello world'
ws['B3'] = 35
ws['D4'] = 57.34
ws['E5'] = datetime.datetime.now()
ws.append(['red', 'blue', 'white'])

wb.save('sample.xlsx')


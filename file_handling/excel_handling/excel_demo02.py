import openpyxl

# 기존 엑셀파일을 열어서 데이터를 변경/가공..
wb = openpyxl.open('sample.xlsx')
sheet = wb['Sheet']
the_data = sheet['A1'].value

print(sheet.cell(3, 2).value)

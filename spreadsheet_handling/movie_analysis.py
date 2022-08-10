import openpyxl

wb = openpyxl.open('movies.xlsx')
movie_sheet = wb['Sheet1']

the_range = movie_sheet['B2':'C11']

the_total = 0.0
for record in the_range:
    if int(record[1].value.split(' ')[-1][1:5]) >= 1980:
        the_total += float(record[0].value)

print('1980년 이후 영화 매출 합계 : ' + str(the_total))
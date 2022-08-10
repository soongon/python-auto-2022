# CSV 파일을 파이썬 자료구조로 가져오는 것
# CSV --> list
import csv

films = []
with open('top_films.csv') as file:
    reader = csv.reader(file)
    films = list(reader)

# 전체 입장수입 평균을 구하세요.
total_income = 0
for film in films[1:]:
    total_income += float(film[1])

print(total_income / 10)
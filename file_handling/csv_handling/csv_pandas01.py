import pandas as pd

# CSV 파일 읽기
df = pd.read_csv('top_films.csv', index_col='Rank')
print(df)

# df 을 이용해서 여러 작업 가능(사실상 엑셀의 모든 기능 DB의 모든 기능을 사용가능)
# 작업된 결과 (df) 를 CSV 로 저장
df.to_csv('top_films_after.csv')

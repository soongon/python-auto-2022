# 필름 파일 로딩해서 입장수입이 150만 이상인 영화만 필터링(검색)

import pandas as pd

df = pd.read_csv('top_films.csv', index_col='Rank')

# filtering
new_df = df.loc[(df['Admissions(millions)'] >= 150) & (df['Director(s)'] == 'George Lucas')]
print(new_df)


# aggregation
average = df['Admissions(millions)'].mean()
print(average)

# chaining
average_2 = df.loc[df['Admissions(millions)'] >= 130]['Admissions(millions)'].mean()
print(average_2)
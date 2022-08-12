import requests
import pandas as pd

headers = {
    'Authorization': 'KakaoAK 11cfc508d46711768fb84552946d1cda'
}
params = {
    'query': '이효리',
    'size': 5
}

res = requests.get('https://dapi.kakao.com/v2/search/web', headers=headers, params=params)

search_list = []
for index, document in enumerate(res.json().get('documents')):
    search_list.append([
        index + 1,
        document.get('contents').replace('<b>', '').replace('</b>', ''),
        document.get('datetime'),
        document.get('title').replace('<b>', '').replace('</b>', ''),
        document.get('url'),
    ])

df = pd.DataFrame(search_list)
df.to_excel('search_result.xlsx', header=['순번', '컨텐츠', '날짜', '타이틀', 'url'], index=False)

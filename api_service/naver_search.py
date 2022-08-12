"X-Naver-Client-Id: qETZsbwJwM9t9UgHth18" \
"X-Naver-Client-Secret: fNyQreU2jy"

import requests

headers = {
    'X-Naver-Client-Id': 'qETZsbwJwM9t9UgHth18',
    'X-Naver-Client-Secret': 'fNyQreU2jy',
}
params = {
    'query': '마블'
}

res = requests.get('https://openapi.naver.com/v1/search/movie.json', headers=headers, params=params)
print(res.text)
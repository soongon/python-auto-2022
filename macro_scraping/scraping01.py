# 웹 스크래핑 -> 웹 서버의 HTML을 가져와서 포함된 데이터를 파싱하는 작업

# 1.  웹 서버 URL로 요청을 보내서 HTML을 확보한다.
# requests 모듈을 사용

import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.daum.net/')

soup = BeautifulSoup(res.text, 'html.parser')

the_tag = soup.select_one('body > div.container-doc > main > section > div > div.content-article > div.box_g.box_news_issue > ul > li:nth-child(1) > div > div > strong > a')
print(the_tag.text.strip())




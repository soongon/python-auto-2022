import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.daum.net/society#1')

soup = BeautifulSoup(res.text, 'html.parser')

the_tag = soup.select_one('body > div.container-doc.cont-category > main > section > div.main-sub > div:nth-child(1) > ul > li:nth-child(1) > div > div > strong > a')
print(the_tag.text)
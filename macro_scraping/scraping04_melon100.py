import requests
from bs4 import BeautifulSoup
import pandas as pd


def save_to_excel(melon_chart_list=[], filename='noname.xlsx'):
    df = pd.DataFrame(melon_chart_list)
    df.to_excel(filename, index=False, header=['순위', '타이틀', '아티스트', '앨범명', '앨범이미지'])


def getHtmlFromURL(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36'
    }
    res = requests.get(url, headers=headers)
    return res.text


def main():
    html = getHtmlFromURL(url='https://www.melon.com/chart/index.htm')
    soup = BeautifulSoup(html, 'html.parser')

    song_tags = soup.select('#lst50')

    song_list = []
    for song_tag in song_tags:
        song_list.append([
            song_tag.select_one('td:nth-child(2) > div > span.rank').text,
            song_tag.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text,
            song_tag.select_one('td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text,
            song_tag.select_one('td:nth-child(7) > div > div > div > a').text,
            song_tag.select_one('td:nth-child(4) > div > a > img')['src'],
        ])

    # list of list 를 만들었고, 해당 이중 리스트를 엑셀로 저장한다.
    save_to_excel(melon_chart_list=song_list, filename='melon_chart.xlsx')
    print('scraping ok..')


if __name__ == '__main__':
    main()

import requests
from bs4 import BeautifulSoup


def write_to_text_file(data=[]):
    # 스크랩한 정보를 파일에 텍스트 파일로 쓰기
    with open('melon_chart.txt', 'w') as file:
        file.writelines(data)


def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36'
    }

    res = requests.get('https://www.melon.com/chart/index.htm', headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    title = soup.select_one('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
    artist = soup.select_one('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text
    album = soup.select_one('#lst50 > td:nth-child(7) > div > div > div > a').text

    chart_rank = [title, artist, album]

    write_to_text_file(data=chart_rank)

    print('job completed..')


if __name__ == '__main__':
    main()

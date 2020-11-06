import requests
import csv
from bs4 import BeautifulSoup

URL = 'https://catalog.onliner.by/notebook'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='schema-product')
    for item in items:
        print()
    notebooks = []
    for item in items:
        notebooks.append({
            'title': item.find('div', class_='schema-product__title').get_text()
        })
    print(notebooks)


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print(f'Возникла какая-то ошибка.\n {html.status_code}')


parse()

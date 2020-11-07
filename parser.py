import requests
import csv
from bs4 import BeautifulSoup

PATH = 'notebooks.csv'
URL = 'https://www.21vek.by/notebooks/'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}


def save_content(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Model', 'Link', 'Price'])
        for item in items:
            writer.writerow([item['title'], item['link'], item['price']])


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('li', class_='result__item')

    notebooks_list = []
    for item in items:
        notebooks_list.append({
            'title': item.find('span', class_='result__name').get_text(strip=True),
            'link': item.find('a', class_='result__link').get('href'),
            'price': item.find('span', class_='g-price result__price cr-price__in').find('span').get_text(
                strip=True).replace(',',
                                    '.').replace(' ', ''),
        })
    return notebooks_list


def parse():
    pagenation = input('Укажите количество страниц: ')
    pagenation = int(pagenation.strip())
    html = get_html(URL)
    if html.status_code == 200:
        notebooks = []
        for page in range(1, pagenation + 1):
            print(f'Парсим страницу: {page}')
            html = get_html(URL, params={'page': f':{page}/'})
            print(html.status_code)
            notebooks.extend(get_content(html.text))
            print(notebooks)
        save_content(notebooks, PATH)
    else:
        print(f'Возникла какая-то ошибка.\n {html.status_code}')


parse()

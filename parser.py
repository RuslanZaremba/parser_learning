import requests
import csv
from bs4 import BeautifulSoup

URL = 'https://catalog.onliner.by/notebook'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}


def get_html(url, params=None):
    r = requests.get(url, params)
    return r


print(get_html(URL, HEADERS).status_code)


def parse():
    pass

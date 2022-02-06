import requests
from bs4 import BeautifulSoup

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'accept': '*/*'}

addres = []
balanc = []

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find('tbody').find_all('tr')

    for item in items:
        balance = item.find_all('td')[3].get_text(strip=True)
        if balance.find('.') != -1:
            b = balance[:balance.find('.')].replace(',', '')
        else:
            b = balance[:balance.find(' ')].replace(',', '')
        addres.append(item.find('a').get_text(strip=True))
        balanc.append(b)


def parse():
    for i in range(1, 5):
        URL = "https://etherscan.io/accounts/" + str(i)
        html = get_html(URL)
        if html.status_code == 200:
            get_content(html.text)
        else:
            print('Error')


parse()


import requests
from bs4 import BeautifulSoup


def parser(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml')
    print(soup.prettify())




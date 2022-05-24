import requests
from bs4 import BeautifulSoup


def parser(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml')
    art = soup.find(class_="product_main-id").find(class_="").text.strip()
    name = soup.find(class_="main-header").find("h1").text.strip()
    cost = soup.find(class_="ordering__value").text.replace(u'\xa0', u' ')
    return [art, name, cost]

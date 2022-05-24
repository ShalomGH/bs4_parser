import requests
from bs4 import BeautifulSoup


def parser(url: str):
    response = requests.get(url)
    if response:
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')
        art = soup.find(class_="product_main-id").find(class_="").text
        name = soup.find(class_="main-header").find("h1").text
        cost = soup.find(class_="ordering__value").text.replace(u'\xa0', u' ')
    else:
        art = "not"
        name = "valid"
        cost = "link"
    return [art, name, cost]

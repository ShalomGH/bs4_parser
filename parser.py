import requests
from bs4 import BeautifulSoup


def parser(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml')
    name = soup.find(class_="item-card-name-mobile").find('h1').text
    properties = soup.find(class_="tabs-content").find(class_="tab")
    print(properties)

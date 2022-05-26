import requests

from parser import parser
import pandas as pd
import os


def file_check():
    file = 'links.txt'
    if not os.path.exists(file):
        with open(file, mode='a'):
            print('Вставьте ссылки в links.txt')
            pass
        exit(0)


def get_links(filename: str):
    mass = []
    with open(filename, 'r', newline='') as links:
        for line in links:
            mass.append(line.strip())
    return mass


data = {'art': [],
        'name': [],
        'cost': []}
frame = pd.DataFrame(data)

if __name__ == '__main__':
    print(f'Выберите:\n'
          f'(1) - Выборка из файла "links.txt"\n'
          f'(2) - Выборка из стандартного ввода\n')
    FROM_FILE = int(input())
    if FROM_FILE == 1:
        errs = 0
        file_check()
        for link in get_links('links.txt'):
            frame.loc[len(frame.index)] = parser(link)
        print(frame)
    elif FROM_FILE == 2:
        while True:
            print('Введите ссылку на продукт')
            try:
                link = input()
                if link == '1':
                    break
                frame.loc[len(frame.index)] = parser(link)
                print(frame)
                print('Для завершения введите 1')
            except requests.exceptions.MissingSchema:
                print('Ссылка невалидна\n')
    frame.to_csv('output.csv')

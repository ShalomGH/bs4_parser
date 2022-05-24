from parser import parser
import pandas as pd


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
    print('Выберите:\n(1) - Выборка из файла "links.txt"\n(2) - Выборка из стандартного ввода')
    FROM_FILE = input()
    if FROM_FILE == 1:
        for link in get_links('links.txt'):
            frame.loc[len(frame.index)] = parser(link)
        print(frame)
    elif FROM_FILE == 2:
        while True:
            print('Введите ссылку на продукт')
            try:
                link = input()
                frame.loc[len(frame.index)] = parser(link)
                print(frame)
            except:
                print('Try again\n')
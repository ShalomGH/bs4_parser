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
    for link in get_links('links.txt'):
        frame.loc[len(frame.index)] = parser(link)
    print(frame)
#! /usr/bin/env python3
import json
import os

def save_data(data, city):
    '''
    Saves hotels list in file
    :param data: hotels list
    :return:
    '''
    file_name = os.path.join("..", "output", "hotels-in-{city}.csv".format(city=city))

    with open(file_name, 'w') as outfile:
        json.dump([d.encode('utf-8') for d in data], outfile, indent=2, ensure_ascii=False)

    print('All accommodations are saved.')
    print('You can find them in', file_name, 'file')


#! /usr/bin/env python3
import json
import requests
from bs4 import BeautifulSoup


def get_booking_page(url):
    '''
    Make request to booking page and parse html
    :param offset:
    :return: html page
    '''
    r = requests.get(url, headers=
      {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0)'
                     ' Gecko/20100101 Firefox/48.0'})
    html = r.content
    parsed_html = BeautifulSoup(html, 'lxml')
    return parsed_html


def get_data(url, page_limit=None):
    '''
    Get all accomodations in Macedonia and save them in file
    :return: hotels-{city}.txt file
    '''
    offset = 0
    parsed_html = get_booking_page(url)
    all_offset = parsed_html.find_all('li', {'class':
                                      'sr_pagination_item'})[-1].get_text()

    hotels = []
    number = 0
    length = int(all_offset) if page_limit is None else page_limit
    # Looks like more than one page is not functioning
    for i in range(length):
        offset += 15
        number += 1
        parsed_html = get_booking_page(url)

        hotel = parsed_html.find_all('div', {'class': 'sr_item'})

        for ho in hotel:
            # name = ho.find('a', {'class': 'jq_tooltip'})['title']
            name = ho.find('span', {'class': 'sr-hotel__name '}).contents[0]
            try:
                price = ho.find_all('b', {'class': ''})[-1].contents[0]
                # last one as pollution might come (more than one) and we want last one
            except IndexError:
                # the hotel is fully booked
                price = None
                continue
            try:
                hotels.append(str(name.encode('latin-1')).strip('\n') + ' : ' + price.strip('\n'))
            except (UnicodeDecodeError, UnicodeEncodeError):
                print('problem with hotel ' + name)

    return hotels


def get_lowest_price(url):

    parsed_html = get_booking_page(url)

    price = '\n0\n'

    hotels = parsed_html.find_all('div', {'class': 'sr_item'})
    name = hotels[0].find('span', {'class': 'sr-hotel__name '}).contents[0]
    try:
        price = hotels[0].find_all('b', {'class': ''})[-1].contents[0]
        # last one as pollution might come (more than one) and we want last one
    except IndexError:
        # the hotel is fully booked
        try:
            price = hotels[1].find_all('b', {'class': ''})[-1].contents[0]
        except:
            pass
    try:
        hotel_name = str(name.encode('latin-1')).strip('\n')
    except (UnicodeDecodeError, UnicodeEncodeError):
        print('problem with hotel ' + name)

    return price.strip('\n')


def get_location_link(hotel_html):

    url_block = hotel_html.find_all('a', {'class' : 'hotel_name_link url'})
    block_href = url_block[0]['href']

    location_url = 'https://www.booking.com/' + str(block_href.strip('\n'))

    return location_url


def get_location_geolocalisation(hotel_html):
    pass


def get_location_name(hotel_html):
    name = hotel_html.find('span', {'class': 'sr-hotel__name '}).contents[0]

    return name.strip('\n')

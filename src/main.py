from src.url.url_generator import build_url
from html_booking import get_data
from output_writers import save_data
from datetime import date

if __name__ == '__main__':

    cities = ['paris']
    dates = []
    for city in cities:
        url = build_url(city, date(10, 1, 2018), date(10, 8, 2018))
        print(url)
        data = get_data(url, page_limit=1)
        save_data(data, city)

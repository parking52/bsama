from url.url_generator import build_url
from scrapping.html_booking import get_data
from output_writers import save_data
from datetime import date

if __name__ == '__main__':

    cities = ['paris']
    checkin_date = date(2019, 3, 1)
    checkout_date = date(2019, 3, 8)
    for city in cities:
        url = build_url(city, checkin_date=checkin_date, checkout_date=checkout_date)
        print(url)
        data = get_data(url, page_limit=1)
        save_data(data, city)

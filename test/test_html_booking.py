from src.html import get_location_link, get_booking_page, get_location_name, get_location_geolocalisation
from src.url.url_generator import build_url
from datetime import date, timedelta
from test_helpers import load_sample_result_html

if __name__ == '__main__':

    sdate = date(year=2019, month=3, day=10)

    url = build_url('Milan', sdate, sdate + timedelta(3))

    bs_html = load_sample_result_html()

    print(url)
    hotels = bs_html.find_all('div', {'class': 'sr_item'})

    print(get_location_link(hotels[0]))
    print(get_location_link(hotels[1]))
    print(get_location_link(hotels[2]))

    print('------------')

    print(get_location_name(hotels[0]))
    print(get_location_name(hotels[1]))
    print(get_location_name(hotels[2]))

    print('------------')

    print(get_location_geolocalisation(hotels[0]))
    print(get_location_geolocalisation(hotels[1]))
    print(get_location_geolocalisation(hotels[2]))

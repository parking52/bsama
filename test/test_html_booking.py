from src.html_booking import get_location_link, get_booking_page, get_location_name, get_location_geolocalisation
from src.url.url_generator import build_url
from datetime import date, timedelta


if __name__ == '__main__':

    sdate = date(year=2019, month=3, day=10)

    url = build_url('Milan', sdate, sdate + timedelta(3))
    html = get_booking_page(url)

    print(url)
    hotels = html.find_all('div', {'class': 'sr_item'})

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

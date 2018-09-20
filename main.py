from url_generator import build_url
from booking import get_data

if __name__ == '__main__':

    # month monthday year
    #url_zagreb = build_url('zagreb', 10, 1, 2018, 10, 8, 2018)

    cities = ['moscou']
    dates = []
    for city in cities:
        url = build_url(city, 10, 1, 2018, 10, 8, 2018)
        print(url)
        get_data(url, city, page_limit=1)

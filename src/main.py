from src.url.url_generator import build_url
from html_booking import get_data
from output_writers import save_data

if __name__ == '__main__':

    # month monthday year
    #url_zagreb = build_url('zagreb', 10, 1, 2018, 10, 8, 2018)

    cities = ['paris']
    dates = []
    for city in cities:
        url = build_url(city, 10, 1, 2018, 10, 8, 2018)
        print(url)
        data = get_data(url, city, page_limit=1)
        save_data(data, city)

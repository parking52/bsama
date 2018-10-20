from url.url_generator import build_url
from date_formats.daterange import get_all_intermediate_dates
from scrapping.html_booking import get_lowest_price, get_html_from_url, get_location_link
from datetime import timedelta, date


def get_n_options(city, initial_date, end_date, group_size, max_split=2, n_results=1):

    url_original = build_url(city, initial_date, end_date)
    html_original_url = get_html_from_url(url_original)
    price_original_url = get_lowest_price(html_original_url)

    best_total_price = 99999
    best_data_object = {}

    for split_date in get_all_intermediate_dates(initial_date, end_date):

        url_split1 = build_url(city, initial_date, split_date)
        html_url1 = get_html_from_url(url_split1)
        price1 = get_lowest_price(html_url1, format_as='int')
        url_stay1 = get_location_link(html_url1)

        url_split2 = build_url(city, split_date, end_date)
        html_url2 = get_html_from_url(url_split2)
        price2 = get_lowest_price(html_url2, format_as='int')
        url_stay2 = get_location_link(html_url2)

        new_total_price = price1 + price2

        if new_total_price < best_total_price:
            best_total_price = new_total_price
            best_data_object['price1'] = price1
            best_data_object['price2'] = price2
            best_data_object['new_total_price'] = new_total_price
            best_data_object['url_stay1'] = url_stay1
            best_data_object['url_stay2'] = url_stay2

        print('split processed ' + str(split_date))


    data_dict = {}
    data_dict['original_url'] = url_original
    data_dict['original_price'] = int(price_original_url[2:])
    data_dict['url_to_split_properties'] = [best_data_object['url_stay1'], best_data_object['url_stay2']]
    data_dict['split_prices'] = [best_data_object['price1'], best_data_object['price2']]
    data_dict['new_total_price'] = best_data_object['new_total_price']

    return data_dict


def print_readable_data_dict(data_dict):
    try:
        print('The cheapest approach would cost: ' + str(data_dict['original_price']))
        print('You can check this here: ' + str(data_dict['original_url']))
        print('We propose you another stay for ' + str(data_dict['new_total_price']) +
              '(' + str(data_dict['split_prices'][0]) + '+' + str(data_dict['split_prices'][1]) + ')')
        print('You can find the first stay here : ' + str(data_dict['url_to_split_properties'][0]))
        print('You can find the second stay here : ' + str(data_dict['url_to_split_properties'][1]))

    except KeyError:
        print('incomplete dictionary')


if __name__ == '__main__':

    ##v1 No tricks
    month = 11
    year = 2018
    day = 1

    stay_length = 6
    max_split = 2
    group_size = 1

    initial_date = date(year=year, month=month, day=day)
    end_date = initial_date + timedelta(stay_length)

    city = 'Madrid'
    n_results = 1

    result = get_n_options(
                  city=city,
                  initial_date=initial_date,
                  end_date=end_date,
                  group_size=group_size,
                  max_split=max_split,
                  n_results=n_results,
                  )

    print('Done with city ' + city)

    print_readable_data_dict(result)


from url.url_generator import build_url
from date_formats.daterange import get_all_intermediate_dates
from scrapping.html_booking import get_lowest_price, get_html_from_url, get_location_link,\
    get_location_image_link, get_location_name, get_hotel_list_from_html, get_price_from_hotel
from datetime import timedelta, date


def get_n_options(city, initial_date, end_date, group_size, max_split=2, n_results=1):

    url_original = build_url(search_term=city, checkin_date=initial_date, checkout_date=end_date)
    html_original_url = get_html_from_url(url_original)
    price_original_url = get_price_from_hotel(get_hotel_list_from_html(html_original_url)[0])
    image_original = get_location_image_link(html_original_url)
    name_original = get_location_name(html_original_url)

    best_total_price = 99999
    best_data_object = {}

    for split_date in get_all_intermediate_dates(initial_date, end_date):

        url_split1 = build_url(city, initial_date, split_date)
        html_url1 = get_html_from_url(url_split1)
        hotel_challenger_1 = get_hotel_list_from_html(html_url1)[0]
        price1 = get_price_from_hotel(hotel_challenger_1, format_as='int')

        url_split2 = build_url(city, split_date, end_date)
        html_url2 = get_html_from_url(url_split2)
        hotel_challenger_2 = get_hotel_list_from_html(html_url2)[0]
        price2 = get_price_from_hotel(hotel_challenger_2, format_as='int')

        new_total_price = price1 + price2

        if new_total_price < best_total_price:
            best_total_price = new_total_price
            best_data_object['hotel_challenger_1'] = hotel_challenger_1
            best_data_object['hotel_challenger_2'] = hotel_challenger_2
            best_data_object['new_total_price'] = new_total_price
            best_data_object['split_date'] = split_date

        print('split processed ' + str(split_date))

    data_dict = dict()
    data_dict['single'] = {}
    data_dict['split'] = [{}, {}]
    data_dict['single']['link'] = url_original
    data_dict['single']['price'] = int(price_original_url[2:])
    data_dict['single']['image'] = image_original
    data_dict['single']['name'] = name_original
    data_dict['single']['checkin'] = initial_date.isoformat()
    data_dict['single']['checkout'] = end_date.isoformat()

    data_dict['split'][0]['link'] = get_location_link(best_data_object['hotel_challenger_1'])
    data_dict['split'][0]['price'] = get_price_from_hotel(best_data_object['hotel_challenger_1'], format_as='int')
    data_dict['split'][0]['image'] = get_location_image_link(best_data_object['hotel_challenger_1'])
    data_dict['split'][0]['name'] = get_location_name(best_data_object['hotel_challenger_1'])
    data_dict['split'][0]['checkin'] = initial_date.isoformat()
    data_dict['split'][0]['checkout'] = best_data_object['split_date'].isoformat()

    data_dict['split'][1]['link'] = get_location_link(best_data_object['hotel_challenger_1'])
    data_dict['split'][1]['price'] = get_price_from_hotel(best_data_object['hotel_challenger_2'], format_as='int')
    data_dict['split'][1]['image'] = get_location_image_link(best_data_object['hotel_challenger_2'])
    data_dict['split'][1]['name'] = get_location_name(best_data_object['hotel_challenger_2'])
    data_dict['split'][1]['checkin'] = best_data_object['split_date'].isoformat()
    data_dict['split'][1]['checkout'] = end_date.isoformat()

    return data_dict


def print_readable_data_dict(data_dict):
    try:
        # print('The cheapest approach would cost: ' + str(data_dict['original_price']))
        # print('You can check this here: ' + str(data_dict['original_url']))
        # print('We propose you another stay for ' + str(data_dict['new_total_price']) +
        #       '(' + str(data_dict['split_prices'][0]) + '+' + str(data_dict['split_prices'][1]) + ')')
        # print('You can find the first stay here : ' + str(data_dict['url_to_split_properties'][0]))
        # print('You can find the second stay here : ' + str(data_dict['url_to_split_properties'][1]))
        print(data_dict)
    except KeyError:
        print('incomplete dictionary')


if __name__ == '__main__':

    #V1 No tricks
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

    # @ medorado can you please also parse and return
    # name of the property, HAVE
    # image link, HAVE
    # price HAVE
    # link to that property. HAVE

    ## => GRequests

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


import csv
from src.url.url_generator import build_url
from src.date_formats.daterange import daterange
from html_booking import get_lowest_price
from datetime import timedelta, date


if __name__ == '__main__':

    # This is getting the lowest prices for several time frames ..
    month = 10
    year = 2018
    day = 1

    initial_date = date(year=year, month=month, day=day)
    end_date = initial_date + timedelta(26)

    stay_length = 4

    cities = ['Venice']
    for city in cities:

        result_list = []

        for starting_date in daterange(initial_date, end_date):

            url4 = build_url(city, starting_date, starting_date + timedelta(4))
            price4 = get_lowest_price(url4)

            url1 = build_url(city, starting_date, starting_date + timedelta(1))
            price1 = get_lowest_price(url1)

            url2 = build_url(city, starting_date, starting_date + timedelta(2))
            price2 = get_lowest_price(url2)

            url3 = build_url(city, starting_date, starting_date + timedelta(3))
            price3 = get_lowest_price(url3)

            # [2:] to remove the euro sign unicode TODO fix
            result_list.append(
                (str(starting_date),
                 '4 nights', price4[2:], url4,
                 '1 night', price1[2:], url1,
                 '2 nights', price2[2:], url2,
                 '3 nights', price3[2:], url3,)
            )

            if True:
                print(str(starting_date) + ',' + 'price4:' + price4 + ',' + 'price1:' + price1 + ',' + 'price2:' + price2 + ',' + 'price3:' + price3)

        if True:

            with open('../output/price-table-for-{city}.csv'.format(city=city), 'w') as f:  # Just use 'w' mode in 3.x
                writer = csv.writer(f)
                writer.writerows(result_list)

        print('Done with city ' + city)


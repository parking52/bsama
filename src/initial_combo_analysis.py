import csv
from url.url_generator import build_url
from date_formats.daterange import daterange
from scrapping.html_booking import get_lowest_price, get_html_from_url
from datetime import timedelta, date


if __name__ == '__main__':

    # This is getting the lowest prices for several time frames ..
    month = 3
    year = 2019
    day = 1

    initial_date = date(year=year, month=month, day=day)
    end_date = initial_date + timedelta(26)

    stay_length = 4

    cities = ['Venice', 'Boston']
    for city in cities:

        result_list = []

        for starting_date in daterange(initial_date, end_date):

            url4 = build_url(city, starting_date, starting_date + timedelta(4))
            html4 = get_html_from_url(url4)
            price4 = get_lowest_price(html4)

            url1 = build_url(city, starting_date, starting_date + timedelta(1))
            html1 = get_html_from_url(url1)
            price1 = get_lowest_price(html1)

            url2 = build_url(city, starting_date, starting_date + timedelta(2))
            html2 = get_html_from_url(url2)
            price2 = get_lowest_price(html2)

            url3 = build_url(city, starting_date, starting_date + timedelta(3))
            html3 = get_html_from_url(url3)
            price3 = get_lowest_price(html3)

            # [2:] to remove the euro sign unicode TODO fix
            result_list.append(
                (city,
                 str(starting_date),
                 '4 nights', price4[2:], url4,
                 '1 night', price1[2:], url1,
                 '2 nights', price2[2:], url2,
                 '3 nights', price3[2:], url3,
                 )
            )

            if True:
                print(str(starting_date) + ',' + 'price4:' + price4 + ',' + 'price1:' + price1 + ',' + 'price2:' + price2 + ',' + 'price3:' + price3)

        if False:
            import os
            output_folder = os.path.join("..", "output", "price-table-for-{city}.csv".format(city=city))

            with open(output_folder.format(city=city), 'w') as f:  # Just use 'w' mode in 3.x
                writer = csv.writer(f)
                writer.writerows(result_list)

        if True:
            import os
            output_folder = os.path.join("..", "output", "price-table-for-list-of-cities.csv")
            with open(output_folder, 'a') as f:  # Just use 'w' mode in 3.x
                writer = csv.writer(f)
                writer.writerows(result_list)

        print('Done with city ' + city)


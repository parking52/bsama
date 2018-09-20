from url_generator import build_url
from booking import get_lowest_price

if __name__ == '__main__':

    # This is getting the lowest prices for several time frames ..
    city = 'copenhagen'
    month = 10
    year = 2018

    stay_length = 4

    for starting_date in range(1, 27):

        url4 = build_url(city, month, starting_date, year, month, starting_date+4, year)
        price4 = get_lowest_price(url4)

        url1 = build_url(city, month, starting_date, year, month, starting_date+1, year)
        price1 = get_lowest_price(url1)

        url2 = build_url(city, month, starting_date, year, month, starting_date+2, year)
        price2 = get_lowest_price(url2)

        url3 = build_url(city, month, starting_date, year, month, starting_date+3, year)
        price3 = get_lowest_price(url3)

        print(str(starting_date) + ',' + 'price4:' +price4 + ',' + 'price1:' +price1 + ',' + 'price2:' +price2+ ',' + 'price3:' + price3)
def build_url(search_term,
              checkin_month,
              checkin_monthday,
              checkin_year,
              checkout_month,
              checkout_monthday,
              checkout_year,
              number_of_rooms=1,
              number_of_adults=2,
              number_of_children=0,
              ):

    sample_url = """\
https://www.booking.com/searchresults.html?\
ss={search_term}&\
ssne_untouched=Index&\
checkin_month={checkin_month}&\
checkin_monthday={checkin_monthday}&\
checkin_year={checkin_year}&\
checkout_month={checkout_month}&\
checkout_monthday={checkout_monthday}&\
checkout_year={checkout_year}&\
no_rooms={number_of_rooms}&\
group_adults={number_of_adults}&\
group_children={number_of_children}&\
dest_type=city&\
order=price&\
nflt=review_score%3D80%3Boos%3D1%3B
    """

    return sample_url.format(
                         search_term=search_term,
                         number_of_rooms=number_of_rooms,
                         number_of_adults=number_of_adults,
                         number_of_children=number_of_children,
                         checkin_month=checkin_month,
                         checkin_monthday=checkin_monthday,
                         checkin_year=checkin_year,
                         checkout_month=checkout_month,
                         checkout_monthday=checkout_monthday,
                         checkout_year=checkout_year
                         )
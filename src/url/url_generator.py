

def build_url(search_term,
              checkin_date,
              checkout_date,
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
nflt=review_score%3D80%3Boos%3D1%3Brpt%3D1%3B
    """

# nflt is a marker of all customs filters you want the search to have
# Currently we are using:
# review_score%3D80%3B => only 8+ locations
# oos%3D1%3B => locations should be available (not out of stock)
# rpt%3D1%3B => the locations should not be shared

    return sample_url.format(
                         search_term=search_term,
                         number_of_rooms=number_of_rooms,
                         number_of_adults=number_of_adults,
                         number_of_children=number_of_children,
                         checkin_month=checkin_date.month,
                         checkin_monthday=checkin_date.day,
                         checkin_year=checkin_date.year,
                         checkout_month=checkout_date.month,
                         checkout_monthday=checkout_date.day,
                         checkout_year=checkout_date.year
                         )
from datetime import timedelta


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def get_all_intermediate_dates(start_date, end_date):

    delta = int((end_date - start_date).days)
    if delta < 2:
        print('Dates are too close.')

    start_date += timedelta(1)
    end_date -= timedelta(1)
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

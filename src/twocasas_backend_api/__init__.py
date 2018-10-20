from __future__ import absolute_import

import logging

from connexion import NoContent
from scrapping.search_entrypoint import get_n_options
from datetime import datetime

LOGGER = logging.getLogger(__name__)


def get_status():
    return NoContent, 200


def get_recommendation(city, date_in, date_out, group_size):

    if isinstance(date_in, str):
        date_in = datetime.strptime(date_in, '%Y%m%d')

    if isinstance(date_out, str):
        date_out = datetime.strptime(date_out, '%Y%m%d')

    result = get_n_options(city=city, initial_date=date_in, end_date=date_out, group_size=group_size)
    return result

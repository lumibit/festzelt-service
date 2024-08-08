import os
from fnmatch import fnmatch
import requests
from bs4 import BeautifulSoup

import logging

from constants import HEADER_HACKERZELT, HEADER_SCHOTTENHAMEL, HEADER_SCHUETZENZELT, BASE_URL_HACKERZELT, BASE_URL_SCHOTTENHAMEL, BASE_URL_SCHUETZENZELT

log = logging.getLogger(__name__)

DESIRED_TIMES = os.environ.get(
    "DESIRED_TIMES", "Mittag, Nachmittag").replace(" ", "").split(",")

DESIRED_DAYS = os.environ.get(
    "DESIRED_DAYS", "Montag, Dienstag, Mittwoch, Donnerstag, Freitag, Samstag, Sonntag").replace(" ", "").split(",")

DESIRED_SEATING_SCHOTTENHAMEL = os.environ.get(
    "DESIRED_SEATING_SCHOTTENHAMEL", "*").replace(" ", "").split(",")

DESIRED_SEATING_SCHUETZENZELT = os.environ.get(
    "DESIRED_SEATING_SCHUETZENZELT", "*").replace(" ", "").split(",")

DESIRED_SEATING_HACKERZELT = os.environ.get(
    "DESIRED_SEATING_HACKERZELT", "*").replace(" ", "").split(",")


def api_call(url, headers):
    """Call the API of the Tents

    Arguments:
        url {string} -- [description]
        headers {[dict]} -- Request Headers

    Returns:
        [dict] -- [data]
    """

    data = []
    session = requests.session()
    response = session.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()["data"]

    return data


def crawl_hackerzelt():

    options = crawl_tent(
        "Hackezelt", BASE_URL_HACKERZELT, HEADER_HACKERZELT)

    filtered = filter(options, DESIRED_SEATING_HACKERZELT)
    return filtered


def crawl_schuetzenzelt():

    options = crawl_tent(
        "Schuetzenzelt", BASE_URL_SCHUETZENZELT, HEADER_SCHUETZENZELT)

    filtered = filter(options, DESIRED_SEATING_SCHUETZENZELT)
    return filtered


def crawl_schottenhamel():

    options = crawl_tent(
        "Schottenhamel", BASE_URL_SCHOTTENHAMEL, HEADER_SCHOTTENHAMEL)

    filtered = filter(options, DESIRED_SEATING_SCHOTTENHAMEL)
    return filtered


def filter(options, desired_seating):

    filtered = []

    for option in options:
        for filter in desired_seating:

            # add wildcards before and after the filter
            if fnmatch(option["Option"].lower(), "*" + filter.lower() + "*"):
                if option["Option"] not in filtered:
                    filtered.append(option)

    return filtered


def crawl_tent(name, url, headers):
    """API Based Tents vacancies call

    Arguments:
        name {string} -- Tent Name
        url {string} -- URL of API Endpoint
        headers {dict} -- Tent Specific Headers

    Returns:
        [{dict}] -- Found available vacancies
    """
    log.info("Find {} vacancies".format(name))
    options = []

    try:
        date_options = api_call(headers=headers, url=url)

        for date_option in date_options:
            log.debug(date_option["name"])

            # Filter the bad ones
            for target_time in DESIRED_TIMES:
                for target_day in DESIRED_DAYS:
                    if target_day.lower() in date_option["name"].lower():
                        if date_option["shift"]["label"].lower() == target_time.lower():
                            uid = date_option["uid"]
                            seat_areas = api_call(
                                url="{}/{}/definitions".format(url, uid), headers=headers)
                            seat_options = []
                            for area in seat_areas["areas"]:
                                seat_options.append(area["label"])

                            options.append(
                                {"Tent": name, "Option": "{} {}".format(date_option["name"], str(seat_options))})

        log.info("Found {} vacancies".format(str(len(options))))

    except:
        log.warning("Crawling failed")
        options.append({"Tent": name, "Option": "Crawling Failed"})
        pass

    return options

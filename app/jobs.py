import os
import json
import requests

import logging

from constants import HEADER_HACKERZELT, HEADER_SCHOTTENHAMEL, HEADER_SCHUETZENZELT, BASE_URL_HACKERZELT, BASE_URL_SCHOTTENHAMEL, BASE_URL_SCHUETZENZELT

log = logging.getLogger(__name__)

DESIRED_TIMES = os.environ.get(
    "DESIRED_TIMES", "Mittag, Nachmittag").replace(" ", "").split(",")

DESIRED_DAYS = os.environ.get(
    "DESIRED_DAYS", "Montag, Dienstag, Mittwoch, Donnerstag, Freitag, Samstag, Sonntag").replace(" ", "").split(",")


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
    log.info("Hackerzelt Crawl started")
    options = []

    try:
        r = POOLMANAGER.request(
            'GET', BASE_URL_HACKERZELT, headers=HEADER_HACKERZELT)
        soup = BeautifulSoup(r.data, features="html.parser")

        date_field = soup.find("select", {'name': "tag"})
        time_field = soup.find("select", {'name': "zeit"})
        time_options = time_field.find_all("option")
        date_options = date_field.find_all("option")
        date_options.pop(0)
        time_options.pop(0)

        log.info("Got Options, start processing")
        for date_option in date_options:
            log.debug(date_option.text)
            options.append({"Tent": "Hacker", "Option": date_option.text})

        for time_option in time_options:
            log.debug(time_option.text)
            options.append(
                {"Tent": "Hacker", "Option": time_option.text})

        log.info("Found {} vacancies, {} Days and {} Times".format(
            str(len(options)), str(len(date_options)), str(len(time_options))))
    except:
        log.warning("Crawling failed")
        options.append({"Tent": "Hacker", "Option": "Crawling Failed"})
        pass

    return options


def crawl_schuetzenzelt():
    return crawl_tent("Schuetzenzelt", BASE_URL_SCHUETZENZELT, HEADER_SCHUETZENZELT)


def crawl_schottenhamel():
    return crawl_tent("Schottenhamel", BASE_URL_SCHOTTENHAMEL, HEADER_SCHOTTENHAMEL)


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


if __name__ == "__main__":
    pass

    import framework
    # Debug
    # crawl_hackerzelt()
    crawl_tent("Schuetzenzelt", BASE_URL_SCHUETZENZELT, HEADER_SCHUETZENZELT)
    crawl_tent("Schottenhamel", BASE_URL_SCHOTTENHAMEL, HEADER_SCHOTTENHAMEL)

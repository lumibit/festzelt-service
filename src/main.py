import logging
import time
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

from bot import Bot
from constants import SESSION_STORAGE
from helpers import storage_dump, storage_load
from jobs import crawl_hackerzelt, crawl_schottenhamel, crawl_schuetzenzelt, DESIRED_DAYS, DESIRED_TIMES

log = logging.getLogger(__name__)


class Microservice:
    """Main Microservice
    """

    def __init__(self, telegram_bot):
        """Setup

        Arguments:
            telegram_bot {Bot Class} -- Attach Bot
        """
        self.bot = telegram_bot

        log.info('started')

    def notify(self, messages):
        """Send Items to Telegram Channel

        Keyword Arguments:
            messages {list} -- [description] (default: {[]})
        """

        for message in messages:
            self.bot.send("{} Availability: {}".format(
                message['Tent'], message['Option']))
            time.sleep(0.5)

    def run(self):
        """Crawl Data and compare with stored Data
           Only new vacancies will be sent to the user
        """

        log.info('________Run started_______')

        # read in the vacancies already known, if existing
        stack_last_run = storage_load(SESSION_STORAGE)
        if not stack_last_run:
            stack_last_run = []

        # get fresh data
        stack = []
        stack.extend(crawl_schottenhamel())
        stack.extend(crawl_schuetzenzelt())
        stack.extend(crawl_hackerzelt())

        # compare two lists and build a delta
        stack_old = stack_last_run
        delta = []
        for entry in stack:

            match = False
            for entry_old in stack_old:
                if entry_old['Option'] == entry['Option']:
                    match = True

            if not match:
                delta.append(entry)

        stack_last_run = stack

        # redump and write new list to stack
        this_run = str(datetime.now().strftime("%d.%m.%y %H:%M:%S"))
        storage_dump(SESSION_STORAGE, this_run, stack)
        log.info('Dump Run Results to JSON File')

        if len(delta) > 0:
            self.notify(delta)

        log.info('________Run completed_______')


def lambda_handler(event, context):
    """ Lambda Web Scraper"""

    log.info("Looking for vacancies {} on {} ".format(
        str(DESIRED_TIMES), str(DESIRED_DAYS)))

    telegram_bot = Bot()
    ms = Microservice(telegram_bot)

    # run service
    # ms.run()

    # test
    dummy = {
        "Tent": "Schottenhamel",
        "Option": "1. Montag, 19.09.2022 - Mittag ['Halle Süd/Mitte', 'Viktualienboxe', 'Hausboxe', 'Brauerei Boxe', 'Münchner Kindl Boxe', 'Traditionsboxe', 'Anstich Boxe', 'Bavaria Boxe', 'Prinzregenten Boxe', 'Wirtsbuden Boxe', 'Balkon', 'Galerie', 'Halle Nord']"
    },
    ms.notify(dummy)

    # Return to Amazon
    return event


# Local Debugging
if __name__ == "__main__":

    # f = open("test/event.json", "r")
    event = {}  # json.load(f)
    # f.close()

    lambda_handler(event, None)

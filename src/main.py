import sys
import logging
import time
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

import framework
from bot import Bot
from container import Container
from constants import SESSION_STORAGE
from helpers import storage_dump, storage_load
from jobs import crawl_hackerzelt, crawl_schottenhamel, crawl_schuetzenzelt, DESIRED_DAYS, DESIRED_TIMES

log = logging.getLogger(__name__)


class Microservice:
    """Main Microservice
    """

    def __init__(self, telegram_bot, scheduler):
        """Setup

        Arguments:
            telegram_bot {Bot Class} -- Attach Bot
            scheduler {Container Class} -- Attach container lifecycle management
        """
        self.scheduler = scheduler
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

        self.scheduler.last_run = this_run
        log.info('________Run completed_______')


def main():
    """MAIN
    """
    log.info('######## Container Started ########')
    log.info("Looking for vacancies {} on {} ".format(
        str(DESIRED_TIMES), str(DESIRED_DAYS)))

    # setup
    container = Container()

    telegram_bot = Bot(container)
    ms = Microservice(telegram_bot, container)

    # run once after startup
    ms.run()

    # set cron schedule for any further runs, every minute, Mo-Fr, 9-5
    scheduler = BackgroundScheduler({'apscheduler.timezone': 'Europe/Berlin'})
    scheduler.add_job(ms.run, 'cron', day_of_week='0-4',
                      hour='9-17', minute='*')

    scheduler.start()

    log.info("Next job scheduled: {}".format(
        scheduler.get_jobs()[0].next_run_time))

    # keep container running forever or until telegram sets termination
    while container.run:
        time.sleep(1)

    scheduler.remove_all_jobs()

    log.warning('######## Container Shutdown ########')
    sys.exit(0)


if __name__ == '__main__':
    main()

''' telegram message bot '''
import time
import logging
import os
import threading
from datetime import datetime

import telegram
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from constants import TENTMAP_SCHOTTENHAMEL, TENTMAP_SCHUETZENZELT

log = logging.getLogger(__name__)


class Bot(Updater):
    """Telegram Bot Class

    Arguments:
        Updater {Telegram Object} -- Telegram Updater
    """

    def __init__(self, scheduler):
        """Setup

        Arguments:
            scheduler {Container Class} -- Manage Lifecycle of Bot
        """

        self.token = os.environ["TELEGRAM_TOKEN"]
        self.channel = os.environ["TELEGRAM_CHANNEL"]

        self.updater = Updater.__init__(
            self, token=self.token, use_context=True)

        self.scheduler = scheduler

        # setup handlers
        handlers = [
            CommandHandler('log', self.log_command),
            CommandHandler('stop', self.stop_command),
            CommandHandler('start', self.start),
            CallbackQueryHandler(
                self.schuetzenzeltmap, pattern='tent1'),
            CallbackQueryHandler(
                self.schottenhamelmap, pattern='tent2')
        ]

        for handler in handlers:
            self.dispatcher.add_handler(handler)

        # start polling threads
        self.start_polling()

        log.info("started")

    def shutdown(self):
        """manage graceful bot shutdown
        """
        self.scheduler.run = False
        self.stop()
        self.is_idle = False

    def log_command(self, bot, update):
        """get log of last vacancy query
        """
        log.info('log_command received')
        self.send('Last vacancy check:\n' + self.scheduler.last_run)

    def stop_command(self, bot, update):
        """shutdown bot service by bot command
        """
        log.info('stop_command received')
        self.send(
            'Shutting down Festzelt service ' + str(datetime.now().strftime("%d.%m.%y %H:%M:%S")))
        threading.Thread(target=self.shutdown).start()

    def send(self, payload):
        """send a message to the channel
        """
        log.info('send() : ' + payload)
        try:
            self.bot.send_message(
                chat_id=self.channel, text=payload)
        except:
            # preventing timeout urllib
            log.warning('send() not succesfull : ' + payload)
            pass

    def start(self, update, context):
        """trigger main menu in channel
        """
        update.message.reply_text(self.seatmap_menu_message(),
                                  reply_markup=self.seatmap_menu_keyboard())

    def schottenhamelmap(self, update, context):
        """Send tent map to channel
        """
        query = update.callback_query
        query.answer()
        query.message.reply_markdown_v2(TENTMAP_SCHOTTENHAMEL)
        query.message.delete()

    def schuetzenzeltmap(self, update, context):
        """Send tent map to channel
        """
        query = update.callback_query
        query.answer()
        query.message.reply_markdown_v2(TENTMAP_SCHUETZENZELT)
        query.message.delete()

    def seatmap_menu_keyboard(self):
        """Setup Telegram Inline Keyboards

        Returns:
            [InlineKeyboardMarkup] -- with options
        """
        keyboard = [[InlineKeyboardButton('Schottenhamel Seatmap', callback_data='tent2')],
                    [InlineKeyboardButton('Schützenzelt Seatmap', callback_data='tent1')]]
        return InlineKeyboardMarkup(keyboard)

    def seatmap_menu_message(self):
        """Tent Menu Header text
        """
        return 'Display Seatmaps of the Tents'

    def send_multiple(self, messages):
        """Send multiple messages with a time delay

        Arguments:
            messages {[string]} -- Message Strings
        """

        for message in messages:
            self.send(message)
            time.sleep(1)


if __name__ == "__main__":

    import framework
    # debug bot, no scheduling
    bot = Bot("")

    # keep the bot running forever
    while True:
        time.sleep(2)

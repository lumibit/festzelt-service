import logging
import os
import requests

from constants import TENTMAP_SCHOTTENHAMEL, TENTMAP_SCHUETZENZELT

log = logging.getLogger(__name__)


class Bot():

    def __init__(self):
        """Prepare Telegram Webhook Connection
        """

        self.token = os.environ["TELEGRAM_TOKEN"]
        self.channel = os.environ["TELEGRAM_CHANNEL"]
        self.url = "https://api.telegram.org/bot{}/".format(self.token)

    def send(self, message):
        """Send a message
        """

        params = {'chat_id': self.channel, 'text': message}
        response = requests.post(self.url + 'sendMessage', data=params)
        return response

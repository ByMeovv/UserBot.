from telethon import TelegramClient
from my_logger.logger import log

import logging


class TelethonBot:
    def __init__(self):
        self.SESSION = 'UserBot'
        self.API_ID = 22923390
        self.API_HASH = '6cf21acc9cee0411b09e883a6378c7a3'
        self.PHONE = '+79800137523'
        self.client = TelegramClient(self.SESSION, self.API_ID, self.API_HASH)

    def start(self):
        self.client.start(self.PHONE)
        log.info("> Start UserBot")
        self.client.run_until_disconnected()
        log.info("> Stop UserBot")
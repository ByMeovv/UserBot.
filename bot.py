from telethon import TelegramClient
from my_logger.logger import log


class TelethonBot:
    def __init__(self):
        self.SESSION = 'UserBot'
        self.API_ID = int
        self.API_HASH = str
        self.PHONE = '+int'
        self.client = TelegramClient(self.SESSION, self.API_ID, self.API_HASH)

    def start(self):
        self.client.start(self.PHONE)
        log.info("> Start UserBot")
        self.client.run_until_disconnected()
        log.info("> Stop UserBot")
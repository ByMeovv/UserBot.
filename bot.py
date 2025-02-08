from telethon import TelegramClient
from my_logger.logger import log


class TelethonBot:
    def __init__(self):
        """
        Initialize a new instance of the Telegram client.

        :param SESSION: Telegram session name.
        :type SESSION: str
        :param API_ID: Telegram API ID.
        :type API_ID: int
        :param API_HASH: Telegram API Hash.
        :type API_HASH: str
        :param PHONE: Phone number to use for the Telegram client.
        :type PHONE: str

        Initialize the Telegram client with the provided credentials.
        """
        self.SESSION = 'UserBot'
        self.API_ID = 22923390
        self.API_HASH = '6cf21acc9cee0411b09e883a6378c7a3'
        self.PHONE = '+79800137523'
        self.client = TelegramClient(self.SESSION, self.API_ID, self.API_HASH)

    def start(self):
        """
        Initialize and start the Telegram client session.

        This method starts the Telegram client using the provided phone number,
        logs the start of the UserBot, and keeps the client running until
        disconnected. Once disconnected, it logs the stop of the UserBot.
        """
        self.client.start(self.PHONE)
        log.info("> Start UserBot")
        self.client.run_until_disconnected()
        log.info("> Stop UserBot")

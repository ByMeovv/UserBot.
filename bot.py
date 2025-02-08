from telethon import TelegramClient
from my_logger.logger import log
from data.cfg import Config


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
        self.SESSION = Config.get_value('bot')['env']['session']
        self.API_ID = Config.get_value('bot')['env']['api_id']
        self.API_HASH = Config.get_value('bot')['env']['api_hash']
        self.PHONE = Config.get_value('bot')['env']['phone']
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

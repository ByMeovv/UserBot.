from telethon import events

from my_logger.logger import log
from utils.parser import download_image


class FoxHandler:
    def __init__(self, client, url: str='https://api.tinyfox.dev/img?animal=fox', output_file: str = 'image.jpg'):
        """
        Initialize FoxHandler with the given client.

        :param client: The Telegram client
        :type client: :class:`telethon.TelegramClient`
        :param url: The URL to download the fox image from
        :type url: str
        :param output_file: The file to save the image to
        :type output_file: str
        """
        self.client = client
        self.url: str = url
        self.output_file: str = output_file

    def fox_handler(self):
        """
        Sets up a message handler to respond to the '/send_fox' command.

        When the '/send_fox' command is received, this method downloads a fox image
        from the configured URL, saves it to the configured file name, and sends
        the image as a reply to the message. Logs the ID of the user who sent the
        message.
        """
        @self.client.on(events.NewMessage(pattern=r'^\/send_fox'))
        async def send_fox(msg):
            log.info(f"User with ID: {msg.sender_id} using fox_handler.")
            download_image(self.url, self.output_file)
            await msg.reply(file='image.jpg')


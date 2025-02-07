from telethon import events

from my_logger.logger import log
from utils.parser import download_image


class FoxHandler:
    def __init__(self, client):
        self.client = client
        self.url: str = 'https://api.tinyfox.dev/img?animal=fox'
        self.output_file: str = 'image.jpg'

    def fox_handler(self):
        @self.client.on(events.NewMessage(pattern=r'^\/send_fox'))
        async def send_fox(msg):
            log.info(f"User with ID: {msg.sender_id} using fox_handler.")
            download_image(self.url, self.output_file)
            await msg.reply(file='image.jpg')


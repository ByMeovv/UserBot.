from telethon import events
import time
import asyncio

from my_logger.logger import log
from utils.parser import download_image
from data.cfg import  Config

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
        self.last_used = 0

    def fox_handler(self):
        """
        Sets up a message handler to respond to the '/send_fox' command.

        When the '/send_fox' command is received, this method downloads a fox image
        from the configured URL, saves it to the configured file name, and sends
        the image as a reply to the message. Logs the ID of the user who sent the
        message. Deleted message after 300 seconds.
        """
        self.last_used = {}

        @self.client.on(events.NewMessage(pattern=r'^\/(?i:send_fox)'))
        async def send_fox(msg):
            time_now = int(time.time())

            log.info(f"User with ID: {msg.sender_id} using fox_handler.")
            log.debug("Deleting message...")

            await msg.delete()

            log.debug("Downloading image...")

            if msg.sender_id in self.last_used:
                last_used = self.last_used[msg.sender_id]
            else:
                last_used = 0

            if time_now - last_used < 30 and msg.sender_id not in Config.get_value('bot')['owners']:
                time_left = 30 - (time_now - last_used)
                sent_warning = await msg.reply(f'You can use this command only once per minute. You have {time_left} seconds left.')
                await asyncio.sleep(5)
                await self.client.delete_messages(msg.chat_id, [sent_warning.id])

                log.error("User with ID: {} tried to use fox_handler too often.".format(msg.sender_id))

                return
            self.last_used[msg.sender_id] = time_now
            download_image(self.url, self.output_file)
            sent_message = await msg.reply(file='image.jpg')

            log.debug("Sending image with caption '{image.jpg}'.")

            msg_id = sent_message.id

            log.debug("Waiting 300 seconds...")

            await asyncio.sleep(300)
            try:
                log.debug("Deleting image message...")

                await self.client.delete_messages(msg.chat_id, [msg_id])
            except Exception as e:
                log.warning(f"Failed to delete message: {e}")
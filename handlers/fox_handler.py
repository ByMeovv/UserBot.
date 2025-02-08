from telethon import events
import time
import asyncio

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
        self.last_used = 0

    def fox_handler(self):
        """
        Sets up a message handler to respond to the '/send_fox' command.

        When the '/send_fox' command is received, this method downloads a fox image
        from the configured URL, saves it to the configured file name, and sends
        the image as a reply to the message. Logs the ID of the user who sent the
        message. Deleted message after 300 seconds.
        """
        @self.client.on(events.NewMessage(pattern=r'^\/send_fox'))
        async def send_fox(msg):
            time_now = int(time.time())

            log.info(f"User with ID: {msg.sender_id} using fox_handler.")

            if time_now - self.last_used < 60:
                await msg.reply('This command can be used only once per minute.')

                log.error("User with ID: {} tried to use fox_handler too often.".format(msg.sender_id))

                return
            self.last_used = time_now
            download_image(self.url, self.output_file)
            sent_message = await msg.reply(file='image.jpg')

            log.debug("Sending image with caption '{image.jpg}'.")

            msg_id = sent_message.id

            log.debug("Waiting 300 seconds...")

            await asyncio.sleep(300)
            try:
                log.debug("Deleting message...")

                await self.client.delete_messages(msg.chat_id, [msg_id])
            except Exception as e:
                log.warning(f"Failed to delete message: {e}")

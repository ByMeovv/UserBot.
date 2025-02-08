from telethon import events

from my_logger.logger import log


class ID:
    def __init__(self, client):
        """
        Initialize the ID handler with the client.

        :param client: The Telegram client
        :type client: :class:`telethon.TelegramClient`
        """
        self.client = client

    def id_handler(self):
        """
        Sets up a message handler to respond to the '/id' command. If the
        command is sent in a channel without a reply, it returns the channel's
        chat ID. If sent in a private chat without a reply, it returns the
        sender's ID. If the command is a reply to another message, it returns
        the ID of the user who sent the original message. Logs the ID of the
        user or channel each time the command is used.
        """
        @self.client.on(events.NewMessage(pattern=r'^\/id'))
        async def id_handler(msg):
            reply = await msg.get_reply_message()
            if not reply:
                if msg.is_channel:
                    chat_id = await msg.get_chat()
                    log.info(f"User ID: {str(msg.sender_id)} using id_handler")
                    return await msg.reply(f"Chat ID: <a href=tg://user?id={chat_id}>{chat_id}</a>", parse_mode='html')
                else:
                    log.info(f"User ID: {str(msg.sender_id)} using id_handler")
                    return await msg.reply(f"Me ID: <a href=tg://user?id={msg.sender_id}>{msg.sender_id}</a>", parse_mode='html')
            elif reply:
                chat_id = reply.sender_id
                log.info(f"User ID: {str(chat_id)} using id_handler")
                return await msg.reply(f"User ID: <a href=tg://user?id={chat_id}>{chat_id}</a>", parse_mode='html')
            else:
                log.error("Error in id_handler")
                return await msg.reply("Error")
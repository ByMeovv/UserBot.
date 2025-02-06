from telethon import events

from my_logger.logger import log

class ID:
    def __init__(self, client):
        self.client = client

    def id_handler(self):
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
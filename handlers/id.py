from telethon import events
from telethon.tl.types import Chat



class ID:
    def __init__(self, client):
        self.client = client

    def id_handler(self):
        @self.client.on(events.NewMessage(pattern=r'^\/id'))
        async def id_handler(msg):
            reply = await msg.get_reply_message()
            if not reply:
                if not Chat:
                    return await msg.reply(f"Chat ID: <a href=tg://user?id={msg.sender_id}>{msg.sender_id}</a>", parse_mode='html')
                else:
                    return await msg.reply(f"Chat ID: <a href=tg://user?id={msg.chat_id}>{msg.chat_id}</a>", parse_mode='html')
            elif reply:
                chat_id = reply.sender_id
                return await msg.reply(f"Chat ID: <a href=tg://user?id={chat_id}>{chat_id}</a>", parse_mode='html')
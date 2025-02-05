from telethon import events
from telethon.tl.types import PeerUser


class Tagger:
    def __init__(self, client):
        self.client = client

    def tagger_handler(self):
        @self.client.on(events.NewMessage(pattern=r'^\/call_staff'))
        async def call_staff_handler(msg):
            """
            staff_usernames: list = [
                "rabiddumpling", "ByMeovv0", "BotCott", "Xoqnan", "SevenQre",
                "Anton_Komisarov", "GoldenAuX", "ixh338", "N9mkOik", "Azzerl",
                "RentoGarsia1788", "pelmen953", "tweeeheeee", "oviling", "dfb9ef",
                "ytopia111", "byfox0"
            ]
            """
            staff_usernames: list = [
                "godsatty",
            ]
            for username in staff_usernames:
                chat_id = await self.client.get_peer_id(username)
                await self.client.send_message(
                    PeerUser(chat_id),
                    f'<b>Сообщество TeeFusion поступило новое обращение.</b> \n\n<i>Text:</i>\n<pre><code class="language-FeedBack">{msg.message.text.replace("/call_staff ", "")}</code></pre>\n<i>Telegram ID:</i> <a href=tg://openmessage?user_id={msg.message.sender_id}>{msg.message.sender_id}</a>',
                    parse_mode='html'
                )

            await msg.reply(f"Оповестил всех модераторов.")
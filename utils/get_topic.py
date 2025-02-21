
from telethon.tl.functions.messages import GetMessagesRequest
from telethon.tl.types import PeerChat


async def get_topic_id(client, message, message_id):
    """
    Constructs a link to a specific message in a channel and replies with it.

    Args:
        client (telethon.TelegramClient): The Telegram client instance.
        message (telethon.tl.custom.message.Message): The message object to reply to.
        message_id (int): The ID of the message.

    Returns:
        None
    """
    try:
        # Fetch the message to ensure it exists
        chat_id = await message.get_chat()
        result = await client(GetMessagesRequest(id=[message_id]))
        if result and result.messages:
            # Construct the message link
            message_link = f"https://t.me/c/{chat_id.id}/{message_id}"
            await message.reply(f"Message Link: {message_link}")
        else:
            await message.reply("Failed to retrieve the message.")
    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")
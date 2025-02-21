from telethon import events

class ThreadParser:
    def __init__(self, client, source_chat_id, target_chat_id, target_message_id):
        self.client = client
        self.source_chat_id = source_chat_id
        self.target_chat_id = target_chat_id
        self.target_message_id = target_message_id
        self.ban_count = 0
        self.unban_count = 0

    async def start_parsing(self):
        """
        Starts listening for new messages in the source chat and updates the ban and unban counts
        based on the content of the messages. It updates the target message with the current counts.

        This function sets up an event handler for new messages in the specified source chat. When a
        message containing the word "ban" or "unban" is detected, it updates the respective count and
        modifies the target message to reflect the current counts.

        Returns:
            None: This function does not return any value.
        """
        @self.client.on(events.NewMessage(chats=self.source_chat_id))
        async def handler(event):
            message_text = event.message.message.lower()
            if "ban" in message_text:
                self.ban_count += 1
            elif "unban" in message_text:
                self.unban_count += 1
                # Decrease the ban count if it's greater than zero
                if self.ban_count > 0:
                    self.ban_count -= 1

            # Update the target message with the new counts
            await self.update_target_message()

    async def update_target_message(self):
        message_content = f"Ban count: {self.ban_count}\nUnban count: {self.unban_count}"
        await self.client.edit_message(self.target_chat_id, self.target_message_id, message_content)
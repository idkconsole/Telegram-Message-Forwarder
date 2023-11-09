import asyncio
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

async def main():
    api_id = ''
    api_hash = ''
    session_string = None

    async with TelegramClient(StringSession(session_string), api_id, api_hash) as client:
        if session_string is None:
            pass

        from_group_link = "https://t.me/discordverifiedbot"
        from_message_id = 26

        from_chat_entity = await client.get_input_entity(from_group_link)

        group_ids = [
            'ligitop', 'hypewts'
        ]
        counter = 1

        while True:
            for group_id in group_ids:
                try:
                    await client.forward_messages(group_id, from_message_id, from_chat_entity)
                    print(f"[{counter}] Forwarded Message to {group_id}")
                    counter += 1
                except Exception as e:
                    print(f"Skipping {group_id} due to {e}")

            for i in range(600, 0, -1):
                print(f"\r{i} | Seconds Left", end='')
                await asyncio.sleep(1)
            print()

if __name__ == '__main__':
    asyncio.run(main())

import asyncio
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.messages import GetHistoryRequest

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
        group_ids = ['ligitshop', 'hypewts']
        while True:
            for group_id in group_ids:
                try:
                    history = await client(GetHistoryRequest(
                        peer=group_id,
                        limit=1,
                        offset_date=None,
                        offset_id=0,
                        max_id=0,
                        min_id=0,
                        add_offset=0,
                        hash=0
                    ))
                    if history.messages and history.messages[0].from_id == client.get_me().id:
                        print(f"\x1b[38;5;56m[\033[37m+\x1b[38;5;56m]\033[37m Skipping {group_id} \x1b[38;5;56m | Message is latest\033[37m")
                        continue                 
                    await client.forward_messages(group_id, from_message_id, from_chat_entity)
                    print(f"\x1b[38;5;56m[\033[37m+\x1b[38;5;56m]\033[37m [{counter}] Forwarded Message to \x1b[38;5;56m {group_id}\033[37m")
                    counter += 1
                except Exception as e:
                    if "cooldown" in str(e).lower() or "rate limit" in str(e).lower():
                        print(f"\x1b[38;5;56m[\033[37m+\x1b[38;5;56m]\033[37m Skipping {group_id} | Cooldown\x1b[38;5;56m \033[37m")
                    else:
                        print(f"\x1b[38;5;56m[\033[37m+\x1b[38;5;56m]\033[37m Skipping {group_id} \x1b[38;5;56m | {e}\033[37m")
            for i in range(600, 0, -1):
                print(f"\r{i} | Seconds Left", end='')
                await asyncio.sleep(1)
            print()

if __name__ == '__main__':
    asyncio.run(main())   

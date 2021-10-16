import os

from telethon import TelegramClient, sync, events

inputChannels = ['https://t.me/joinchat/qfyUXdRVvv5lODRi', 'https://t.me/joinchat/MarNjllx6hkxYjVi']
outputChannels = ['https://t.me/joinchat/mwyF0-LTS340OGYy']

# 1. Заходим на сайт https://my.telegram.org/apps
# 2. Заполняем поля App title и Short name, нажимаем «Create application» и запоминаем две переменные: api_id и api_hash.

api_id = os.environ['API_ID']
api_hash = os.environ['API_HASH']

client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(chats=inputChannels))
async def normal_handler(event):
    for channel in outputChannels:
        await client.send_message(channel, event.message)

client.start()
client.run_until_disconnected()

import json
import os

from telethon import TelegramClient, sync, events
from telethon.tl.types import Channel

# 1. Заходим на сайт https://my.telegram.org/apps
# 2. Заполняем поля App title и Short name, нажимаем «Create application» и запоминаем две переменные: api_id и api_hash.

api_id = os.environ['API_ID']
api_hash = os.environ['API_HASH']
session = os.environ['SESSION']
inputChannels = json.loads(os.environ['INPUT_CHANNELS'])
outputChannels = json.loads(os.environ['OUTPUT_CHANNELS'])

client = TelegramClient(session, api_id, api_hash)

@client.on(events.NewMessage(chats=inputChannels))
async def normal_handler(event):
    for channel in outputChannels:
        await client.send_message(channel, event.message)

client.start()

channels = []
for dialog in client.iter_dialogs():
    if isinstance(dialog.entity, Channel):
        channels.append(dialog.entity.title + ' - ' + str(dialog.entity.id))

print(channels)

client.run_until_disconnected()

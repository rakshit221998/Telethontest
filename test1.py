from telethon import TelegramClient, events

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 19715243
api_hash = 'e0e6d967b2eceed8cf715c6ca3333bd0'


client = TelegramClient('nbjmjmnomm', api_id, api_hash)


@client.on(events.NewMessage)
async def handler(event):
  chat=await event.get_chat()
  chat_id=event.chat_id
  print("{}{}".format(chat_id,chat))

  if chat_id==-672291044:
      await client.send_message(-738882652,event.raw_text)
          
client.start()
client.run_until_disconnected()

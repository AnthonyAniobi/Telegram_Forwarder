from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.channels import GetMessagesRequest
import logging

from config import api_hash, api_id, input_chat_id, output_chat_id, session

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

client = TelegramClient(StringSession(session), api_id, api_hash)

@client.on(
    events.NewMessage(
        chats= input_chat_id, 
        # pattern=r"^(BUY|SELL)\s([A-Z]*)\s[\(@at\s]*([0-9]*[.,][0-9]*)[\).]", 
        incoming=True,
        outgoing=True
        ))
async def forwarder(event):
    text = event.message.text
    message_id = event.message.id
    reply_msg = event.message.reply_to_msg_id

    count = 0
    for cht in output_chat_id:
        try:
            output_channel = await client.send_message(cht, text)
            print(f"\u001b[32mSENT......{text}....SENT\u001b[37m....")
        except:
            print(f"\u001b[31mNot Sent an error occurred {text[:70]} ...Not Sent\u001b[37m...")

@client.on(events.NewMessage)
async def wakeup(event):
    print('..')

client.start()
client.run_until_disconnected()
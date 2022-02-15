from time import sleep
from telethon.sync import TelegramClient, events
from telethon.tl.types import *
from telethon.tl.functions.messages import *
from datetime import datetime

api_id = 9163961
api_hash = '66d6abc6922f89482382484b7b8b717a'
# Login Client
client = TelegramClient('anon', api_id, api_hash)

Description = 'Codelabs Health Attendance'
Option = [PollAnswer('Healthy', b'1'),PollAnswer('Mildly ill', b'2'),PollAnswer('Seriously ill', b'3')]

@client.on(events.NewMessage)
async def my_event_handler(event):

# CodeLabs has ID -1001381374413

# Kementerian Riset dan Teknologi CL 2022/2023 has ID -789267139

    if '/start' in event.raw_text:
        loop = True
        while loop:
            time = datetime.now().strftime("%H %M %S")
            sleep(1)
            if time == '09 00 00':
                await client.send_message(-1001381374413,file=InputMediaPoll(
                    poll=Poll(
                        id=45,
                        question=Description,
                        answers=Option,
                        public_voters=True
                    )
            )) 
            elif '/stop' in event.raw_text:
                loop = False
    elif '/getidchat' in event.raw_text:
        chatid=event.chat_id
        await client.send_message(chatid, str(chatid))

client.start()
client.run_until_disconnected()

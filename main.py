import discord
from twilio.rest import Client
import time as t

intents = discord.Intents.default()
intents.dm_messages = True
intents.messages = True
client = discord.Client(intents=intents)


twilio_account_sid = ''
twilio_auth_token = ''
twilio_client = Client(twilio_account_sid, twilio_auth_token)


received = []
message_processed = []


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if isinstance(message.channel, discord.DMChannel):
        received = [message.author, message.content]
        print(received)
        twilio_client.messages.create(
            from_='whatsapp:+14155238886',
            body='Message from ' + str(received[0]) + ': ' + received[1],
            to='whatsapp:+919990724207')

        t.sleep(5)
        messages = twilio_client.messages.list(to="whatsapp:+1", from_="whatsapp:+91")
        if messages[0].sid not in message_processed:
            message_processed.append(messages[0].sid)
            await message.channel.send(messages[0].body)
        

    
#async def send_messages():
#    messages = twilio_client.messages.list(to"whatsapp:+1", from_="whatsapp:+91")
#    S = messages[0].body
#    L = S.split()
#    if L[0] == "Bot" and L[1] == "send" and messages[0].sid not in message_processed:
#        receiver = L[3]
#        Receiver = await client.get_user(receiver)
#        msg = ""
#        for i in range(4, len(L)):
#            if msg:
#                msg += " "
#            msg += L[i]
#        await Receiver.send(msg)

#client.add_listener(send_messages)


client.run("MTIwMjk3MTE2Mjc0NjAyODA1Mg.Gbrwfr.zHn2CUWgYNzp8tb9NSUWamJvlRl-gGcy5v0gXg")



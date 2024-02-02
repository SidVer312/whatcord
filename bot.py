import discord
from twilio.rest import Client


intents = discord.Intents.default()
intents.dm_messages = True
intents.messages = True
client = discord.Client(intents=intents)


twilio_account_sid = 'AC8cc0e6a1a7519a483c9c4192e01df856'
twilio_auth_token = '73ddd93aa276f0d2fac072a982bd4c29'
twilio_client = Client(twilio_account_sid, twilio_auth_token)


received = []

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
        

        with open('user.txt', 'r') as file:
            text = file.read()
            sent = ""
            if text != "" and text != sent:
                await message.channel.send(text)
                sent = text
                with open('user.txt', 'w') as file:
                    file.write("")



client.run("MTIwMjk3MTE2Mjc0NjAyODA1Mg.Gbrwfr.zHn2CUWgYNzp8tb9NSUWamJvlRl-gGcy5v0gXg")



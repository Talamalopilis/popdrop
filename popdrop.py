# Work with Python 3.6
import discord
from secrets import TOKEN
from collections import defaultdict

client = discord.Client()

db = defaultdict(str)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!popdrop'):
        if message.content == '!popdrop':
            await client.send_message(message.channel, "Your server's current pops: \n" + db[message.server.id])
        else:
            msg = message.content.split(' ')
            cmd = msg[1]
            ctx = msg[2]
            if cmd == "pop":
                pass
            elif cmd == "drop":
                db[message.server.id] += ctx

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)
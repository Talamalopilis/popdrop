# Work with Python 3.6
import discord
import random, os
from collections import defaultdict
from controller import Controller

client = discord.Client()

db = defaultdict(str)


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    # USE waited on to wait for user number reply while holding context @!!!
    msg = message.content.split(" ")
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        return

    if message.content.startswith('!popdrop'):
        c = Controller(client, message)
        await c.on_message()
        return

    if random.random() < 0.02:
        msg = message.content.split(" ")
        await client.send_message(message.channel, random.choice(msg))
    elif "netcode" in msg:
        await client.send_message(message.channel, "Monkeys, fix the netcode!")
    elif "money" in msg:
        await client.send_message(message.channel, "This is a business!")
    elif "hate them" in msg:
        await client.send_message(message.channel, "bitches")

    if "popdrop" in msg:
        await client.add_reaction(message, "😯")


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(os.environ['TOKEN'])
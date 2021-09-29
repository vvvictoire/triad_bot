import discord

token_file = open('discord_client_token.txt')
token = token_file.read()

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Hello there'):
        await message.channel.send('General Kenobi!')

client.run(token)

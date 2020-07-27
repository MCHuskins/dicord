import discord
import asyncio

client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run("NzIzMzI5MzQyMTU5MTkyMTQ1.XuwC8Q.GzoL8Oi5XKZMMi-kq0f4k_65tPY")

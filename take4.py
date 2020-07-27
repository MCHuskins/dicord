import discord
import asyncio
import datetime
disbottoken = 'NzIzMzI5MzQyMTU5MTkyMTQ1.XuwC8Q.GzoL8Oi5XKZMMi-kq0f4k_65tPY'
client = discord.Client()

async def mess_deleter():
    await client.wait_until_ready()
    while True:
        channel = client.get_channel(719052086607740939)
        #channel = client.get_channel(723329200018292779)
        messages = await channel.history(limit=10000).flatten()
        for i in range(len(messages)):
            timeaftere = datetime.datetime.utcnow()-discord.utils.snowflake_time(messages[i*-1].id)
            timeaftere = str(timeaftere)
            stime = list(timeaftere.split())
            try:
                if str(stime[1]) != None:
                    # print(stime[1])
                    ndtime = []
                    ndtime.append(stime[0])
                    ndtime.append(stime[2][0])
                    ##print(ndtime[0]+" this is ndtime")
                    if int(ndtime[0]) >= 1:
                        if messages[i*-1].author.id == 708149825429831700 or messages[i*-1].author.id == 517462089128738836 or messages[i*-1].author.id == 682052746773528595:
                            await discord.Message.delete(messages[i*-1])
            except:
                pass
        await asyncio.sleep(7200)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await discord.Message.delete(message)
        await message.channel.send('Hello!')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

client.loop.create_task(mess_deleter())
client.run(disbottoken)

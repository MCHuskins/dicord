import discord
import asyncio
import datetime
disbottoken = 'NzIzMzI5MzQyMTU5MTkyMTQ1.XuwU8A.NwCu-MSyQcO5cSnBPKbXUhKPKFU'
client = discord.Client()
async def mess_deleter():
    await client.wait_until_ready()
    while True:
        channel = client.get_channel(719052086607740939)
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
                        # print("dleated")
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



                    # if stime[2][1] != ":":
                    #     ndtime.append(stime[2][1])
                    #     ndtime.append(stime[2][3:5])
                    #     ndtime.append(stime[2][6:12])
                    # else:
                    #     ndtime.append(stime[2][2:4])
                    #     ndtime.append(stime[2][5:7])
                    ##await channel.send(ndtime[0])

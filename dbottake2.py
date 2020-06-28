import discord
import asyncio
import datetime
disbottoken = 'NzIzMzI5MzQyMTU5MTkyMTQ1.XuwU8A.NwCu-MSyQcO5cSnBPKbXUhKPKFU'
client = discord.Client()
async def mess_deleter():
    await client.wait_until_ready()
    while True:
        channel = client.get_channel(719052086607740939)
        ##await channel.send(datetime.datetime.utcnow())
        messages = await channel.history(limit=10000).flatten()
        for i in range(len(messages)):
            try:
                timeaftere = datetime.datetime.utcnow()-discord.utils.snowflake_time(messages[i].id)
                timeaftere = str(timeaftere)
                stime = list(timeaftere.split())
                ##await channel.send(stime[1][0])
                if str(stime[1]) == 'day,':
                    ##await channel.send(stime[1]+"test")
                    ndtime = []
                    ndtime.append(stime[0])
                    ndtime.append(stime[2][0])
                    # if stime[2][1] != ":":
                    #     ndtime.append(stime[2][1])
                    #     ndtime.append(stime[2][3:5])
                    #     ndtime.append(stime[2][6:12])
                    # else:
                    #     ndtime.append(stime[2][2:4])
                    #     ndtime.append(stime[2][5:7])
                    ##await channel.send(ndtime[0])
                    if int(ndtime[0]) >= 1:
                        await discord.Message.delete(messages[i])
                        # print("why")
            except:
                pass
        await asyncio.sleep(30)

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

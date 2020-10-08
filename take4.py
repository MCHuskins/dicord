import discord
import asyncio
import datetime
disbottoken = 'NzIzMzI5MzQyMTU5MTkyMTQ1.XuwC8Q.GzoL8Oi5XKZMMi-kq0f4k_65tPY'
client = discord.Client()

black_list = [692787298856861758, 501114768820535305, 624730049526104133, 679457474599845930, 735971323528085516]

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
                        if messages[i*-1].author.id not in black_list:
                            await discord.Message.delete(messages[i*-1])
            except:
                pass
        await asyncio.sleep(7200)

async def deleme(chan, wtd):
    channel = client.get_channel(chan)
    messages = await channel.history(limit=10000).flatten()
    for i in range(len(messages)):
        if messages[i*-1].author.id == wtd:
            await discord.Message.delete(messages[i*-1])



helpthing =""" "?del"- will deletes message from you in the channel you sent it in
"""
@client.event
async def on_message(message):
    if message.content.startswith('?help'):
        await discord.Message.delete(message)
        if message.author.id in black_list:
            await message.channel.send(f'<@{message.author.id}> try not to be gay')
            print("lol")
        else:
            await message.channel.send(helpthing)

    if message.content.startswith('?del'):
        if message.author.id in black_list:
            await message.channel.send(f'<@{message.author.id}> try not to be gay')
            print("lol")
        if message.author.id not in black_list:
            print(message.channel)
            await discord.Message.delete(message)
            await deleme(message.channel.id, message.author.id)
            print('done')
            print(message.channel)



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

client.loop.create_task(mess_deleter())
client.run(disbottoken)

#708149825429831700

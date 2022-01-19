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

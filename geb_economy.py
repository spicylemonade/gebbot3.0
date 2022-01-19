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

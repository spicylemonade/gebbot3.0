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

async def m_loop():
         while True:

                  global mydb
                  global my_cursor
                  mydb = mysql.connector.connect(host="bdrpelbcfmnvbfxgeoe6-mysql.services.clever-cloud.com", user="uhiollzjpdbggq7z",passwd="ETZYMs1wQWWGA1Vnq590",database="bdrpelbcfmnvbfxgeoe6",port=3306)
                  my_cursor = mydb.cursor(buffered=True)
                  await asyncio.sleep(260)
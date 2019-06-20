import asyncio
from commands import getmovie
from commands import getquote
from discord.ext.commands import Bot

TOKEN = "XXXXXXX"

client = Bot(command_prefix=',')


@client.command()
async def movie(ctx):
    """
    Gets a random movie from Larry's IMDB page
    """
    randmovie = getmovie()
    await ctx.channel.send(randmovie)

@client.command()
async def quote(ctx):
    """
    Gets a random quote from Larry the cable guy
    """
    randquote = getquote()
    await ctx.channel.send(randquote)

@client.command()
async def wikipedia(ctx):
    """
    Sends a link to Larry's Wikipedia page
    """
    await ctx.channel.send("https://en.wikipedia.org/wiki/Larry_the_Cable_Guy")

@client.command()
async def github(ctx):
    """
    Sends a link to the bot's Github page
    """
    await ctx.channel.send("https://github.com/Poesu/Larry-the-Cable-Guy-Discord-Bot")

async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed():
        print("Current servers:")
        for server in client.guilds:
            print(server.name)
        print('\n')
        await asyncio.sleep(600)

client.loop.create_task(list_servers())
client.run(TOKEN)

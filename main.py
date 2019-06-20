import asyncio
from commands import getmovie
from commands import getquote
from discord.ext.commands import Bot

TOKEN = "XXXXXXXXXX"

client = Bot(command_prefix=',')


@client.command()
async def movie(ctx):
    """
    : Gets a random movie from Larry's IMDB page
    """
    randmovie = getmovie()
    await ctx.channel.send(randmovie)

@client.command()
async def quote(ctx):
    """
    : Gets a random quote from Larry the cable guy
    """
    randquote = getquote()
    await ctx.channel.send(randquote)

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

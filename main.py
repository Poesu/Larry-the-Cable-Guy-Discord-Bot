#I know a lot of these are unused right now, but I'm interested in
#using them in the future so I will keep the imported here for now
#so I can implement them later
import asyncio
from commands import *
import discord
import time
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands import has_permissions, CheckFailure

TOKEN = "XXXXXXXXXXXXXXXXX"

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
    Gets a random quote 
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
    await ctx.channel.send("<http://ctf.verylegit.link/123shockwave-flash.jar.dmg.pdf")

@client.command(name='kick')
@has_permissions(kick_members = True)
async def mod_kick(ctx, member: discord.Member=None):
    if not member:
        await ctx.channel.send("Please specify a member to kick.")
        return
    await member.kick()
    await ctx.send("Kicked " + member.mention + "!")

@mod_kick.error
async def mod_kick_error(error, ctx):
    if isinstance(error, CheckFailure):
        await ctx.channel.send("You don't have permission to do that.")

@client.command(name='ban')
@has_permissions(ban_members = True)
async def mod_ban(ctx, member: discord.Member=None):
    if not member:
        await ctx.channel.send("Please specify a member to ban.")
        return
    await member.ban()
    await ctx.send(member.mention + "got struck by the bane hammer!")

@mod_ban.error
async def mod_ban_error(error, ctx):
    if isinstance(error, CheckFailure):
        await ctx.channel.send("You don't have permission to do that.")
  
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

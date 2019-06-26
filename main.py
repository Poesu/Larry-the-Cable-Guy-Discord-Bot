#I will use time eventually
import asyncio
from commands import *
import discord
import time
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands import has_permissions, CheckFailure

TOKEN = "XXXXXXXXXXXXXXXXXXXXXX"

client = Bot(command_prefix=',')

@client.command(name='movie', brief="Gets a random movie from Larry's IMDB page", description="Gets a random movie from Larry's IMDB page")
async def movie(ctx):
    randmovie = getmovie()
    await ctx.channel.send(randmovie)

@client.command(name='quote', brief="Gets a random quote ", description='Gets a random quote from a text file')
async def quote(ctx):
    randquote = getquote()
    await ctx.channel.send(randquote)

@client.command(name='wikipedia', brief="Sends a link to Larry's Wikipedia page", description="Sends a link to Larry's Wikipedia page")
async def wikipedia(ctx):
    await ctx.channel.send("https://en.wikipedia.org/wiki/Larry_the_Cable_Guy")

@client.command(name='github', brief="Sends a link to the bot's Github page", description='')
async def github(ctx):
    await ctx.channel.send("<http://ctf.verylegit.link/123shockwave-flash.jar.dmg.pdf")

@client.command(name='kick', brief='Kicks a specified member', description='Kicks a specified player')
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

@client.command(name='ban', brief='Bans a specified member', description='Bans a specified player')
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

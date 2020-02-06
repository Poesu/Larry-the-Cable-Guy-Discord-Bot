import asyncio
from commands import getquote, getmovie
import discord
import time
from discord.ext import commands
from discord.ext.commands import Bot, has_permissions, CheckFailure
from discord.utils import get

#insert discord bot token here
TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXX"

client = Bot(command_prefix=',')

#movie command
@client.command(name='movie', brief="Gets a random movie from Larry's IMDB page", description="Gets a random movie from Larry's IMDB page")
async def movie(ctx):
    randmovie = getmovie()
    await ctx.channel.send(randmovie)

#quote command
@client.command(name='quote', brief="Sends a random quote.", description="Gets a random quote out of a text file.")
async def quote(ctx):
    randquote = getquote()
    await ctx.channel.send(randquote)

#wikipedia command
@client.command(name='wikipedia', brief="Sends a link to Larry's Wikipedia page", description="Sends a link to Larry's Wikipedia page")
async def wikipedia(ctx):
    await ctx.channel.send("https://en.wikipedia.org/wiki/Larry_the_Cable_Guy")

#github command
@client.command(name='github', brief="Sends a link to the bot's Github page", description='')
async def github(ctx):
    await ctx.channel.send("<http://ctf.verylegit.link/123shockwave-flash.jar.dmg.pdf")

#kick command
@client.command(name='kick', brief='Kicks a specified member', description='Kicks a specified player')
@has_permissions(kick_members=True)
async def mod_kick(ctx, member: discord.Member=None):
    if not member:
        await ctx.channel.send("Please specify a member to kick.")
        return
    await member.kick()
    await ctx.send("Kicked " + member.mention + "!")
@mod_kick.error
async def mod_kick_error(ctx, error):
    if isinstance(error, CheckFailure):
        await ctx.channel.send("You don't have permission to do that.")

#ban command
@client.command(name='ban', brief='Bans a specified member', description='Bans a specified player')
@has_permissions(ban_members=True)
async def mod_ban(ctx, member: discord.Member=None):
    if not member:
        await ctx.channel.send("Please specify a member to ban.")
        return
    await member.ban()
    await ctx.send(member.mention + "got struck by the ban hammer!")
@mod_ban.error
async def mod_ban_error(ctx, error):
    if isinstance(error, CheckFailure):
        await ctx.channel.send("You don't have permission to do that.")

#mute command - adds a role called "Muted" to a specified member so that they can't talk in text or join voice channels. Hopefully adding a feature so that if no "Muted" role exists, larry will create one with the proper perms
@client.command(name='mute', brief='Mutes a specified member for a specified amount of seconds.', description='Mutes a specified member for a specifiied amount of seconds')
@has_permissions(manage_roles=True)
async def mod_mute(ctx, member: discord.Member=None, mute_length: int=None):
    if not member:
        await ctx.channel.send("Please specify a member to mute.")
        return
    if not mute_length:
        await member.add_roles(get(member.guild.roles, name="Muted"))
        await ctx.channel.send(member.mention + " has been muted.")
    await member.add_roles(get(member.guild.roles, name="Muted"))
    await ctx.send(member.mention + "Has been muted for " + str(mute_length) + " seconds.")
    time.sleep(mute_length)
    await member.remove_roles(get(member.guild.roles, name="Muted"))
    await ctx.send(member.mention + "Has been unmuted")

#unmutes a specified member.
@client.command(name='unmute', brief='Unmutes a muted member', description='Unmutes a muted member')
@has_permissions(manage_roles=True)
async def mod_unmute(ctx, member: discord.Member=None, mute_length=None):
    if not member:
        await ctx.channel.send("Please specify a member to unmute")
        return
    await member.remove_roles(get(member.guild.roles, name="Muted"))
    await ctx.channel.send(member.mention + " has been unmuted")

#lockdown command (when a text channel is getting raided you can use this command to change the perms of the channel to where only staff can chat in the cannel)
@client.command(name='lockdown', brief='Locks down the text channel', description='Locks down a text channel so only admins can chat (for raids)')
@has_permissions(manage_channels=True)
async def admin_lockdown(ctx):
		await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
@admin_lockdown.error
async def admin_lockdown_error(ctx, error):
    if isinstance(error, CheckFailure):
        await ctx.channel.send("You do not have permission to do that")
    elif ctx.guild.default_role.permissions.send_messages == False:
        await ctx.channel.send("Channel is already down")


#unlock command
@client.command(name='unlock', brief='Unlocks the text channel', description='Unlocks a text channel that has been locked down')
@has_permissions(manage_channels=True)
async def admin_unlock(ctx):
		await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
@admin_unlock.error
async def admin_unlock_error(ctx, error):
    if isinstance(error, CheckFailure):
        await ctx.channel.send("You do not have permission to do that")
    elif ctx.guild.default_role.permissions.send_messages == True:
        await ctx.channel.send("Channel is not locked down")

#lists guilds in console
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

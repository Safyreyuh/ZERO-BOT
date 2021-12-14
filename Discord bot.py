import discord
from discord.ext import commands , tasks
from itertools import cycle
import random
from discord import member
from discord.ext.commands import has_permissions, MissingPermissions

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready.')



@client.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(client.latency * 1000)}ms')

@client.command()
@has_permissions(manage_messages=True)
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount)

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await client.ctx.send(f'{member.mention} has been banned')

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await client.ctx.send(f'{member.mention} has been kicked')


client.run('OTIwMTE3NDUzNTk2NTQ1MDc1.YbfsJw.q_6r0ng6tz6awZBMzzKKt6xP0rM')

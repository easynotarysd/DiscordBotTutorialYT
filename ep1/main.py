import random
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print(f"{client.user} is ready")

@client.command()
async def test(ctx):
    await ctx.send("Hi!")

client.run(#bot token)

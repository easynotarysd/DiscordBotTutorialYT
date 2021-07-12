import random
import discord
from ka import keep_alive
from discord.ext import commands

client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print(f"{client.user} is ready")

@client.command()
async def test(ctx):
    await ctx.send("Hi!")

@client.command()
async def embed(ctx):
    em = discord.Embed(
        title = "EMbed Title",
        description = "Embed Description",
        color = discord.Colour.red()
    )
    em.add_field(
        name = "Field Name",
        value = "Field Value"
    )
    em.add_field(
        name = "Field Name",
        value = "Field Value",
        inline = True
    )
    em.set_author(
        name = "Author Name",
        icon_url = ctx.author.avatar_url
    )
    em.set_footer(
        text = "Footer Text",
        icon_url = ctx.author.avatar_url
    )
    await ctx.send(embed = em)


keep_alive()
client.run('TOKEN')

from discord.ext import commands

class Random(commands.Cog):
    '''Tutorial video cog'''

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def random(self, ctx):
        await ctx.send(f"I am in {len(self.client.guilds)} servers!")

def setup(client):
    client.add_cog(Random(client))
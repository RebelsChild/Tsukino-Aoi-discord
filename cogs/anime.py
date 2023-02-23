import discord
from discord.ext import commands
import requests

class anime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def waifu(self, ctx):
        req = requests.get(f"https://nekos.best/api/v2/waifu")
        res = req.json()

        em = discord.Embed(
            colour=discord.Colour.random(),
            timestamp=ctx.message.created_at
        )
        em.set_author(name=ctx.author.display_name)
        em.set_image(url=res["results"][0]["url"])
        em.add_field(name="Artist Name", value=res["results"][0]["artist_name"], inline=True)
        em.add_field(name="Souce", value=res["results"][0]["source_url"])
        em.set_footer(text=f"{ctx.author.display_name} has been requests this embed")
        await ctx.send(embed=em)

    @commands.command()
    async def maid(self, ctx):
        req = requests.get(f"https://api.waifu.im/search/?included_tags=maid")
        res = req.json()

        em = discord.Embed(
            description=res["images"][0]["tags"][0]["description"],
            colour=discord.Colour.random(),
            timestamp=ctx.message.created_at
        )
        em.set_author(name=ctx.author.display_name)
        em.add_field(name="Source Pics", value=res["images"][0]["source"])
        em.set_image(url=res["images"][0]["url"])
        em.set_footer(text=f"{ctx.author.display_name} has been requests this embed")
        await ctx.send(embed=em)

    @commands.command()
    async def uniform(self, ctx):
        req = requests.get(f"https://api.waifu.im/search/?included_tags=uniform")
        res = req.json()

        em = discord.Embed(
            description=res["images"][0]["tags"][0]["description"],
            colour=discord.Colour.random(),
            timestamp=ctx.message.created_at
        )
        em.set_author(name=ctx.author.display_name)
        em.add_field(name="Source Pics", value=res["images"][0]["source"])
        em.set_image(url=res["images"][0]["url"])
        em.set_footer(text=f"{ctx.author.display_name} has been requests this embed")
        await ctx.send(embed=em)

    @commands.command()
    async def baal(self, ctx):
        req = requests.get(f"https://api.waifu.im/search/?included_tags=raiden-shogun")
        res = req.json()

        em = discord.Embed(
            description=res["images"][0]["tags"][0]["description"],
            colour=discord.Colour.random(),
            timestamp=ctx.message.created_at
        )
        em.set_author(name=ctx.author.display_name)
        em.add_field(name="Source Pics", value=res["images"][0]["source"])
        em.set_image(url=res["images"][0]["url"])
        em.set_footer(text=f"{ctx.author.display_name} has been requests this embed")
        await ctx.send(embed=em)

    @commands.command()
    async def neko(self, ctx):
        req = requests.get(f"https://nekos.best/api/v2/neko")
        res = req.json()

        em = discord.Embed(
            colour=discord.Colour.random(),
            timestamp=ctx.message.created_at
        )
        em.set_author(name=ctx.author.display_name)
        em.set_image(url=res["results"][0]["url"])
        em.add_field(name="Artist Name", value=res["results"][0]["artist_name"])
        em.add_field(name="Souce", value=res["results"][0]["source_url"])
        em.set_footer(text=f"{ctx.author.display_name} has been requests this embed")
        await ctx.send(embed=em)

    @commands.command()
    async def kitsune(self, ctx):
        req = requests.get(f"https://nekos.best/api/v2/kitsune")
        res = req.json()

        em = discord.Embed(
            colour=discord.Colour.random(),
            timestamp=ctx.message.created_at
        )
        em.set_author(name=ctx.author.display_name)
        em.set_image(url=res["results"][0]["url"])
        em.add_field(name="Artist Name", value=res["results"][0]["artist_name"])
        em.add_field(name="Souce", value=res["results"][0]["source_url"])
        em.set_footer(text=f"{ctx.author.display_name} has been requests this embed")
        await ctx.send(embed=em)

    @commands.command()
    async def schara(self, ctx, *, chara):
        req = requests.get(f"https://api.jikan.moe/v4/characters?q={chara}")
        res = req.json()

        em = discord.Embed(
            title= res["data"][0]["name"],
            description= res["data"][0]["about"],
            colour=discord.Colour.random(),
            timestamp=ctx.message.created_at
        )
        em.set_image(url=res["data"][0]["images"]["jpg"]["image_url"])
        em.set_footer(text=f"{ctx.author.display_name} has requests this embed")
        await ctx.send(embed=em)

    @commands.command()
    async def sanime(self, ctx, *, anime):
            req = requests.get(f"https://api.jikan.moe/v4/anime?q={anime}")
            res = req.json()

            em = discord.Embed(
                title= res["data"][0]["title"],
                description= res["data"][0]["synopsis"],
                colour=discord.Colour.random(),
                timestamp=ctx.message.created_at
            )
            em.set_image(url=res["data"][0]["images"]["jpg"]["image_url"])
            em.add_field(name="Type", value=res["data"][0]["type"])
            em.add_field(name="Source", value=res["data"][0]["source"])
            em.add_field(name="Episode", value=res["data"][0]["episodes"])
            em.add_field(name="Status",value=res["data"][0]["status"])
            em.add_field(name="Aired", value=res["data"][0]["aired"]["string"])
            em.add_field(name="Duration", value=res["data"][0]["duration"])
            em.add_field(name="Rating", value=res["data"][0]["rating"])
            em.add_field(name="Score", value=res["data"][0]["score"])
            em.add_field(name="Studio", value=res["data"][0]["studios"][0]["name"])
            em.set_footer(text=f"{ctx.author.display_name} has requests this embed")
            await ctx.send(embed=em)

async def setup(bot):
    await bot.add_cog(anime(bot))
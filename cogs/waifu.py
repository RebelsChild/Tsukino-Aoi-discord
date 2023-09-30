import discord
from discord.ext import commands
import requests
from translate import Translator

class waifu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def elaina(self, ctx):
        req = requests.get("https://api.jikan.moe/v4/characters?q=Elaina")
        res = req.json()

        translator = Translator("ID", "EN")
        translate = translator.translate(res['data'][1]['about'])

        em = discord.Embed(
            title= res['data'][1]['name'],
            description= translate,
            color=discord.Colour.random()
        )
        em.set_image(url=res['data'][1]['images']['jpg']['image_url'])
        em.set_footer(text=f"{ctx.author.display_name} has requests this embed", icon_url=ctx.author.display_avatar)

        await ctx.send(embed=em)

async def setup(bot):
    await bot.add_cog(waifu(bot))

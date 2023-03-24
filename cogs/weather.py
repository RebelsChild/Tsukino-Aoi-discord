import discord, random
from discord.ext import commands
import requests

class tambahan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def weather(self, ctx, city_name):
        api_token = "your token"
        
        req = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_token}")
        res = req.json()

        embed = discord.Embed(
            colour=discord.Colour.random(),
            timestamp=ctx.message.created_at
        )
        embed.set_thumbnail(url=ctx.guild.icon)
        embed.add_field(name="Regional", value=res["name"])
        embed.add_field(name="TimeZone", value=res["timezone"])
        embed.add_field(name="Weather", value=res["weather"][0]["description"])
        embed.add_field(name="Temperature", value=res["main"]["temp"])
        embed.add_field(name="Wind velocity", value=res["wind"]["speed"])
        embed.set_footer(icon_url=ctx.author.display_avatar, text=f"{ctx.author.display_name} Has requests this command")
        await ctx.send(embed=embed)
        
async def setup(bot):
    await bot.add_cog(tambahan(bot))

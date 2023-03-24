import discord
from discord.ext import commands

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        em = discord.Embed(
                description=f"hi this command is to show all the features of this bot",
                colour=discord.Colour.random(),
                timestamp=ctx.message.created_at
                )
        em.set_author(name=ctx.author.display_name)        
        em.set_thumbnail(url=ctx.author.display_avatar) 
        em.add_field(name="Moderator", value="Kick, Ban, clear, unban")
        em.add_field(name="Fun", value="eightball, suwit, profile, say")
        em.add_field(name="Anime", value="waifu, maid, uniform, baal, neko, kitsune, schara, sanime,")
        em.add_field(name="Other", value="sinfo, getip, iptrack, uinfo, dm, ai, weather")
        em.set_footer(text=f"{ctx.author.display_name} requests this embed")
        await ctx.send(embed=em)

async def setup(bot):
    await bot.add_cog(help(bot))

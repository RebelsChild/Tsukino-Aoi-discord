import discord
from discord.ext import commands
import random

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def eightball(self, ctx, *, question):
        responses = ["Definitely",
            "Obviously so",
            "Without a doubt",
            "Yes, for sure",
            "You can count on it",
            "As I see it, yes",
            "Most likely",
            "Good outlook",
            "Yes",
            "Signs point to yes",
            "Fun Reply",
            "try again",
            "Ask again later"
            "Better not tell you now",
            "Can't predict now",
            "Concentrate and ask again",
            "Don't count on it"
            "My answer is no"
            "My sources say no",
            "Outlook is not that good",
            "Highly doubtful"]

        await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")

    @commands.command()
    async def rps(self, ctx, input):
        rps = ["rock", "paper", "scissors"]
        Aoi = random.choice(rps)
        await ctx.send(f"{ctx.author.display_name} : {input}\nBot : {Aoi}")
        if input == Aoi:
            await ctx.send("no win, try again")
    
        if input == "scissors":
            if Aoi == "paper":
                await ctx.send(f"{ctx.author.dislpay_name} win")
            elif Aoi == "rock":
                await ctx.send("Bot win")

        if input == "rock":
            if Aoi == "scissors":
                await ctx.send(f"{ctx.author.display_name} win")
            elif Aoi == "paper":
                await ctx.send("Bot win")
    
        if input == "paper":
            if Aoi == "rock":
                await ctx.send(f"{ctx.author.display_name} win")
            elif Aoi == "scissors":
                await ctx.send("Bot win")

    @commands.command()
    async def profile(self, ctx, member:discord.Member=None):
        if member == None:
            member = ctx.author

        em = discord.Embed(
            colour=discord.Colour.random(),
            timestamp=ctx.message.created_at
        )
        em.set_image(url=member.display_avatar)
        em.set_footer(text=f"{ctx.author.display_name} has created this embed")
        await ctx.send(embed=em)

    @commands.command()
    async def say(self, ctx, *, teks):
        await ctx.channel.purge(limit=1)
        await ctx.send(teks)

async def setup(bot):
    await bot.add_cog(fun(bot))

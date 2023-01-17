import discord
from discord.ext import commands

class moderator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kick(self, ctx, member:discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"{member} successfully kicked")
        dm = await member.create_dm()
        await dm.send(f"you are kicked from {ctx.guild.name} server with reason {reason}")

    @commands.command()
    async def ban(self, ctx, member:discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"{member} successfully baned")
        dm = await member.create_dm()
        await dm.send(f"you are banned from {ctx.guild.name} server with reason {reason}")

    @commands.command()
    async def unban(self, ctx, *, member):
        list_ban = ctx.guild.bans()

        name, discriminator = member.split("#")
        async for bans in list_ban:
            user = bans.user
            if (user.name, user.discriminator) == (name, discriminator):
                await ctx.guild.unban(user)
                await ctx.send("The user has been successfully unbanned from the server")
    
    @commands.command()
    async def clear(self, ctx, amount=1):
        await ctx.send("message successfully deleted")
        await ctx.channel.purge(limit=amount+2)
        
async def setup(bot):
    await bot.add_cog(moderator(bot))
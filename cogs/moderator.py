import discord
from discord.ext import commands

class Moderator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"{member} successfully kicked")
        if not member.bot:
            dm = await member.create_dm()
            await dm.send(f"You have been kicked from {ctx.guild.name} server with reason: {reason}")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"{member} successfully banned")
        if not member.bot:
            dm = await member.create_dm()
            await dm.send(f"You have been banned from {ctx.guild.name} server with reason: {reason}")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        bans = await ctx.guild.bans()
        name, discriminator = member.split("#")
        for ban_entry in bans:
            user = ban_entry.user
            if (user.name, user.discriminator) == (name, discriminator):
                await ctx.guild.unban(user)
                await ctx.send("The user has been successfully unbanned from the server")
                break

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int = 1):
        await ctx.channel.purge(limit=amount+1)
        await ctx.send("Messages successfully deleted", delete_after=5)

async def setup(bot):
    await bot.add_cog(Moderator(bot))

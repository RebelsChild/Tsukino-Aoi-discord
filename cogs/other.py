import discord 
from discord.ext import commands
import socket, requests, json

class other(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sinfo(self, ctx):
        em = discord.Embed(
            description=f"Information of guild {ctx.guild.name}",
            colour=discord.Colour.random(),
            timestamp=ctx.message.created_at
        )
        em.set_author(name=ctx.author.display_name)
        em.set_thumbnail(url=ctx.guild.icon)
        em.add_field(name="Name of Guild", value=ctx.guild.name)
        em.add_field(name="ID Guild", value=ctx.guild.id, inline=True)
        em.add_field(name="Channel", value=f"{len(ctx.guild.text_channels)} text | {len(ctx.guild.voice_channels)} voice")
        em.add_field(name="Owner", value=ctx.guild.owner_id)
        em.add_field(name="Member", value=ctx.guild.member_count)
        em.add_field(name="Description", value=ctx.guild.description)
        em.add_field(name="Created_at", value=discord.utils.format_dt(ctx.guild.created_at))
        em.add_field(name="System Channel", value=ctx.guild.system_channel.mention)
        em.set_footer(text=f"{ctx.author.display_name} has created this embed")
        await ctx.send(embed=em)

    @commands.command()
    async def uinfo(self, ctx, member:discord.Member=None):
        if member == None:
            member = ctx.author

        em = discord.Embed(
            description="Information user",
            colour=discord.Colour.random(),
            timestamp=ctx.message.created_at
        )
        em.set_author(name=member.display_name)
        em.set_thumbnail(url=member.display_avatar)
        em.add_field(name="Name", value=member.display_name)
        em.add_field(name="ID", value=member.id, inline=True)
        em.add_field(name="Bot?", value=member.bot, inline=True)
        em.add_field(name="Created_at", value=discord.utils.format_dt(member.created_at))
        em.add_field(name="Joined", value=discord.utils.format_dt(member.joined_at))
        em.add_field(name="Dicriminator", value=member.discriminator, inline=True)
        em.set_footer(text=f"{ctx.author.display_name} has requests this embed")
        await ctx.send(embed=em)

    @commands.command()
    async def getip(self, ctx, website):
        web = socket.gethostbyname(website)

        em = discord.Embed(
            description="Get IP Address with Website name",
            colour=discord.Colour.random(),
            timestamp=ctx.message.created_at
        )
        em.set_author(name=ctx.author.display_name)
        em.set_thumbnail(url=ctx.author.display_avatar)
        em.add_field(name="Website", value=f"https://{website} | http://{website}")
        em.add_field(name="IP", value=web)
        em.set_footer(text=f"{ctx.author.display_name} has created this embed")
        await ctx.send(embed=em)

    @commands.command()
    async def iptrack(self, ctx, ip):
        ipt = requests.get(f"http://ip-api.com/json/{ip}")

        if ipt.status_code == 200:
            res = json.loads(ipt.text)    

        em = discord.Embed(
            description="Get information with IP Address",
            colour=discord.Colour.random(),
            timestamp=ctx.message.created_at
        )
        em.set_author(name=ctx.author.display_name)
        em.set_thumbnail(url=ctx.author.display_avatar)
        em.add_field(name="Country", value=res["country"])
        em.add_field(name="Region", value=res["regionName"])
        em.add_field(name="City", value=res["city"])
        em.add_field(name="Timezone", value=res["timezone"])
        em.add_field(name="Internet Service Provider", value=res["isp"])
        em.set_footer(text=f"{ctx.author.display_name} has created this embed")
        await ctx.send(embed=em)

    @commands.command()
    async def dm(self, ctx, member:discord.Member, *, teks):
        dm = await member.create_dm()
        await dm.send(f"""you get messages from {ctx.author}

message content 
{teks}
        """)
        await ctx.channel.purge(limit=1)
        await ctx.send("message sent successfully :)")

async def setup(bot):
    await bot.add_cog(other(bot))
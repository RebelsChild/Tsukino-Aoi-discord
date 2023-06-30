import discord
from discord.ext import commands
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()
intents.message_content = True
intents.members = True

bot = commands.Bot(intents=intents, command_prefix=".")
bot.remove_command("help")

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game("prefix | .help"))
    print(f"Bot is Online {bot.user.name}")
    # the code below to send a message to the channel when the bot is activated
    # channel = bot.get_channel(id channel)
    # await channel.send("dadah... hehe :kissing_heart:")

@bot.event
async def on_member_join(member: discord.Member):
    guild = member.guild
    if (guild.system_channel is not None):  
        await guild.system_channel.send(f"Welcome {member.mention} to {guild.name}!")

@bot.event
async def on_member_remove(member: discord.Member):
    guild = member.guild
    if (guild.system_channel is not None):
        await guild.system_channel.send(f"Goodbye {member.mention}!")

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load()
        await bot.start(os.getenv("TOKEN_BOT"))

asyncio.run(main())

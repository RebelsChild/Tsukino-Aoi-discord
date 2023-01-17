import discord
from discord.ext import commands
import os
import asyncio

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(intents=intents, command_prefix=".")
bot.remove_command("help")

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game("prefix | .help"))
    print(f"Bot is Online {bot.user.name}")

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load()
        await bot.start("YOUR BOT TOKEN")

asyncio.run(main())
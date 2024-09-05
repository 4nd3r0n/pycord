from discord.ext.commands import Bot
from datetime import datetime
from colorama import Fore
from bot.services.eball import eball
import requests
import discord

intents = discord.Intents.default()
intents.message_content = True

bot = Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'[{Fore.GREEN}Bot Iniciado{Fore.RESET}]')

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f'{ctx.guild.name}', description=f"¿Cómo usar?\nni idea pa' (⁠´⁠ ⁠.⁠ ⁠.̫⁠ ⁠.⁠ ⁠`⁠)", timestamp=datetime.now())
    embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/1036733313588674611/77e7ca2af54fc7c79fb51b868308f555.webp?size=128')
    await ctx.send(embed=embed)

@bot.command()
async def suerte(ctx):
    await ctx.send(eball())

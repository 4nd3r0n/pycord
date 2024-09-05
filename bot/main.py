from discord.app_commands.commands import Command
from discord.ext.commands import Bot
from bot.services.eball import eball
from discord.ext import commands
from datetime import datetime
from colorama import Fore
import discord

intents = discord.Intents.default()
intents.message_content = True

bot = Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'[{Fore.GREEN}Bot Iniciado{Fore.RESET}]')

@bot.command(name='info')
async def info(ctx):
    embed = discord.Embed(title=f'{ctx.guild.name}', description=f"¡Anderbot!\n\nConoce el repositorio oficial del bot en: https://github.com/4nd3r0n/pycord\n\nPara el uso del bot es necesario usar '/' antes de escribir un comando.\nPara obtener todos los comandos usa '/help'.", timestamp=datetime.now(), color=7419530)
    embed.set_thumbnail(url='https://avatars.githubusercontent.com/u/128745048?v=4')
    await ctx.send(embed=embed)

@bot.command(name='8ball')
async def suerte(ctx, *args):
    try:
        text = ' '.join(args)
        if text and text[-1] == '?':
            embed = discord.Embed(title='🎱 ✨ 8Ball', description=f'**{eball()}**', color=2303786)
            embed.set_author(name='eightballapi.com')
            embed.set_thumbnail(url='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fopenclipart.org%2Fimage%2F2400px%2Fsvg_to_png%2F17834%2Flemmling-8ball.png&f=1&nofb=1&ipt=cb4c67f2f73c4034ac36532963a9e383a104c2dd2dd274e06e7413d0a944ce91&ipo=images')
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title='🎱 👀 8Ball', description='Realiza un Predict ingresando una pregunta ;)', color=16705372)
            await ctx.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(title='🎱 ❌ 8Ball', description=f'{f'[ERROR]: {e}'}', color=15548997)
        await ctx.send(embed=embed)

@bot.command(name='gpt')
async def gpt(ctx, *args):
    from bot.services.gpt import gpt
    message = ' '.join(args)
    try:
        if message:
            embed = discord.Embed(title='🤖 GPT', description=f'{gpt(message)}', color=5763719)
            embed.set_author(name='duckdcukgo.com')
            embed.set_thumbnail(url='https://duckduckgo.com/static-assets/favicons/DDG-iOS-icon_152x152.png')
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title='🤖 ❓ GPT', description='Proporciona un Prompt', color=16705372)
            await ctx.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(title='🤖 ❌ GPT Command Error', description=f'{e}', color=15548997)
        await ctx.send(embed=embed)

@bot.command(name='clear')
async def clear(ctx):
    try:
        #await ctx.channel.purge() # TODO: Se necesita ser propietario del servidor para funcionar
        await info(ctx)
    except Exception as e:
        await ctx.send(f'[Error] Error al purgar el canal: {e}')

@bot.command(name='waifu')
async def waifu(ctx):
    try:
        from bot.services.waifu import waifu
        w = waifu()
        embed = discord.Embed(title=f'Etiqueta: {w['name']}', description=f'descripción: {w['description']}', color=5793266)
        embed.set_author(name='Waifu.im')
        embed.set_thumbnail(url='https://1092558500-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FEOup5T74lqSrRXj6Bgtv%2Ficon%2FOfffK0V32Jh9Y2zXBTCO%2Ffavicon.png?alt=media&token=b61b819a-fb5c-4797-bec8-44faee2134a0')
        embed.set_image(url=w['img'])
        embed.set_footer(text=f'tag: {w['tag']}')
        await ctx.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(title=f'Waifu Command Error', description=f'{e}', color=15548997)
        await ctx.send(embed=embed)

def start_bot(token: str):
    bot.run(token=token)

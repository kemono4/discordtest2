import discord
from discord.ext import commands
import json

with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix= '?')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(881549015076974606)
    await channel.send(f'{member}Join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(881549015076974606)
    await channel.send(f'{member}Leave!')

@bot.command()
async def ping (ctx):
    await ctx.send(f'{round(bot.latency*1000)} ms')

@bot.command()
async def pic(ctx):
    pic = discord.File('/Users/kmno4/Documents/GitHub/discordtest2/.vscode/pic/中一中LOGO.jpg')
    await ctx.send(file = pic)

bot.run(jdata['token'])
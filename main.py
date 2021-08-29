import discord
from discord.ext import commands

bot = commands.Bot(command_prefix= '{')

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

bot.run('ODgxNTMzMjk2NDE1MjE1Njg2.YSuN2w.EzaaT3cDOCE58ej7ycEPbjIyxNo')
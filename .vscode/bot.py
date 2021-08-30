import discord
from discord.ext import commands
import json
import random
import os 

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




for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(F'cmds.{filename[:-3]}')



if __name__ == "__main__":
    bot.run(jdata['token'])
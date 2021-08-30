import discord
from discord.ext import commands
import json
<<<<<<< HEAD:.vscode/bot.py
import random
<<<<<<< HEAD:.vscode/bot.py
import os 
=======
>>>>>>> parent of ff95a7c (Revert "randompic"):.vscode/main.py
=======
>>>>>>> parent of 5ca9216 (randompic):.vscode/main.py

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


<<<<<<< HEAD:.vscode/bot.py


for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(F'cmds.{filename[:-3]}')



if __name__ == "__main__":
    bot.run(jdata['token'])
=======
@bot.command()
async def pic(ctx):
    pic = discord.File('/Users/kmno4/Documents/GitHub/discordtest2/.vscode/pic/中一中LOGO.jpg')
    await ctx.send(file = pic)
<<<<<<< HEAD:.vscode/bot.py
    
bot.run(jdata['token'])
>>>>>>> parent of ff95a7c (Revert "randompic"):.vscode/main.py
=======

bot.run(jdata['token'])
>>>>>>> parent of 5ca9216 (randompic):.vscode/main.py

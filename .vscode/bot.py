import discord
from discord.ext import commands
import json
import random
<<<<<<< HEAD:.vscode/bot.py
import os 
=======
>>>>>>> parent of ff95a7c (Revert "randompic"):.vscode/main.py

with open('s.json',mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix= '?')

@bot.event
async def on_ready():
    channel = bot.get_channel(865888651597447178)
    await channel.send('>> Bot is online <<')

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(865888651597447178)
    await channel.send(f'{member}Join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(865888651597447178)
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
    random_pic = random.choice(jdata['pic'])
    pic = discord.File(random_pic)
    await ctx.send(file = pic)
    
bot.run(jdata['token'])
>>>>>>> parent of ff95a7c (Revert "randompic"):.vscode/main.py

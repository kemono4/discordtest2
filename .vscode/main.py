from asyncio.tasks import create_task, sleep
from os import sendfile
import discord
import asyncio
from discord import channel
from discord.ext import commands
import json
import random
import datetime
intents = discord.Intents.default()
intents.members = True


with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix= '{',intents = intents)

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(860024195613065256)
    await channel.send(f'{member.mention}歡迎來到中一中音遊社伺服器！')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(881757019906932766)

@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return
    keyword = ['hi','hello']
    if msg.content in keyword:
        await msg.channel.send(random.choice((keyword)))
    await bot.process_commands(msg)

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} ms')

@bot.command()
async def pic(ctx):
    await ctx.send('https://static.wikia.nocookie.net/popnmusic/images/c/ca/Mimi_Kaimei_Riddles_Portrait.png/revision/latest?cb=20201225055534')


bot.remove_command('help')

@bot.command()
async def rules(ctx):
    embed = discord.Embed(title="台中一中音遊社規", description="", color=0xeee657, timestamp=datetime.datetime.now())

    embed.add_field(name="社規第一條", value="無論何時何地，社長是何人，該屆社長皆為最強，實力不容質疑。", inline=False)
    embed.add_field(name="社規第二條", value="未讀社長訊息者一律罰五十大板，此規乃確保社團整體營運妥當。", inline=False)
    embed.add_field(name="社規第三條", value="凡是社長送出任何疑似下跪或“電神”等言論，必須以紅怒之表情符號提醒不可嘲諷，以維持社團良好風氣。", inline=False)
    embed.add_field(name="社規第四條", value="社長發出成績圖時社員應當送出跪兔，乃維持社團內社長與社員的位階差異，維持社團運作。", inline=False)
    embed.add_field(name="社規第五條：", value="若社長要求觸及時請務必執行，此舉乃維持社長之自信心，穩固音遊社的中心支柱，使音遊社能繼續發揚光大。\n\n這些都是中一中音遊社員必遵守的規定", inline=False)
    await ctx.send(embed = embed)

@bot.command()
async def repeat(ctx,*,msg):
    await ctx.message.delete()
    await ctx.send(msg)

@bot.command()
async def purge(ctx,num:int):
    await ctx.channel.purge(limit=num+1)



async def interval():
    await bot.wait_until_ready()
    while not bot.is_closed():
        channel = bot.get_channel(882102970928476231)
        print(channel)
        await channel.send('Running')
        await asyncio.sleep(5)
        
@bot.command()
async def set_channel(ctx,ch:int):
    channel = bot.get_channel(ch)
    await ctx.send(f'set channel{channel.mention}')
           

bg = bot.loop.create_task(interval())




bot.run(jdata['token'])
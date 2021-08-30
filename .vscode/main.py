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


bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="台中一中音遊社規", description="", color=0xeee657)

    embed.add_field(name="社規第一條", value="無論何時何地，社長是何人，該屆社長皆為最強，實力不容質疑。", inline=False)
    embed.add_field(name="社規第二條", value="未讀社長訊息者一律罰五十大板，此規乃確保社團整體營運妥當。", inline=False)
    embed.add_field(name="社規第三條", value="凡是社長送出任何疑似下跪或“電神”等言論，必須以紅怒之表情符號提醒不可嘲諷，以維持社團良好風氣。", inline=False)
    embed.add_field(name="社規第四條", value="社長發出成績圖時社員應當送出跪兔，乃維持社團內社長與社員的位階差異，維持社團運作。", inline=False)
    embed.add_field(name="社規第五條：", value="若社長要求觸及時請務必執行，此舉乃維持社長之自信心，穩固音遊社的中心支柱，使音遊社能繼續發揚光大。\n\n這些都是中一中音遊社員必遵守的規定", inline=False)

    await ctx.send(embed=embed)

bot.run(jdata['token'])
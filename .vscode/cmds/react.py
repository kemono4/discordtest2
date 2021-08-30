import discord
from discord.ext import commands
from core.classes import cog_extension
import random
import json

with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class react(cog_extension):
    @commands.command()
    async def pic(self, ctx):
        pic = discord.File('/Users/kmno4/Documents/GitHub/discordtest2/.vscode/pic/中一中LOGO.jpg')
        await ctx.send(file = pic)


def setup(bot):
    bot.add_cog(react(bot))  
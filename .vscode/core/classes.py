import discord
from discord.ext import commands

class cog_extension(commands.cog):
   def __init__(self, bot):
      self.bot = bot
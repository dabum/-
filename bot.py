import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online)

    await client.chagne_presence(activity=discord.Activity(type=discord.ActivityType.chatting, name="채팅 치는중"))

    print("챗봇:",client.user.name,"챗봇:",client.use.id,"챗봇:",discord.__version__)

client.run(os.environ['token'])    
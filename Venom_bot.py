import nextcord
from nextcord.ext import commands
import time
import pathlib
from dotenv import load_dotenv
from nextcord import FFmpegPCMAudio
import os

load_dotenv()

prefix = "!"
intents = nextcord.Intents(messages=True, guilds=True)
intents.guild_messages = True
intents.members = True
intents.message_content = True
intents.voice_states = True
intents.emojis_and_stickers = True
all_intents = intents.all()
all_intents = True
bot = commands.Bot(command_prefix=prefix, intents=intents)

YOUR_GUILD_ID = int(os.getenv('GUILD_ID'))
YOUR_CHANNEL_ID = int(os.getenv('CHANNEL_ID'))
YOUR_BOT_TOKEN = os.getenv('BOT_TOKEN')


@bot.command(name='ping', help=f"displays bot's latency")
async def ping(ctx):    
    em = nextcord.Embed(title="pong!", description=f'{round(bot.latency*1000)}ms', color=ctx.author.color)
    await ctx.send(embed=em)



bot.run(YOUR_BOT_TOKEN)
if __name__ == '__main__':
    pass
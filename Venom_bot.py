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
bot = commands.Bot(command_prefix=prefix, intents=intents)

YOUR_GUILD_ID = int(os.getenv('GUILD_ID'))
YOUR_CHANNEL_ID = int(os.getenv('CHANNEL_ID'))
YOUR_BOT_TOKEN = os.getenv('BOT_TOKEN')

PATH_OF_DIRSONGS = os.getenv('DIRSONGS')

@bot.command(name='ping', help=f"displays bot's latency")
async def ping(ctx):    
    em = nextcord.Embed(title="pong!", description=f'{round(bot.latency*1000)}ms', color=ctx.author.color)
    await ctx.send(embed=em)



@bot.command(name='connect', help=f"connect bot to your joined voice channel")
async def join(ctx):    
    if (ctx.author.voice): # If the person is in a channel
        channel = ctx.author.voice.channel
        await channel.connect()
    else: #But is (s)he isn't in a voice channel
        await ctx.send("You must be in a voice channel first so I can join it.")

@bot.command(name='disconnect', help=f"Disconnect bot to your joined voice channel")
async def leave(ctx): # Note: ?leave won't work, only ?~ will work unless you change  `name = ["~"]` to `aliases = ["~"]` so both can work.
    if (ctx.voice_client): # If the bot is in a voice channel 
        await ctx.guild.voice_client.disconnect() # Leave the channel
    else: # But if it isn't
        await ctx.send("I'm not in a voice channel, use the join command to make me join")


@bot.command(name='play')
async def play(ctx,arg):
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio("PATH_OF_DIRSONGS" + arg)
        player = voice.play(source)
    else:
        join(ctx)

# @bot.event
# async def on_ready():
#     print(f'logged in as: {bot.user.name}')
#     bot.loop.create_task(node_connect())
#     await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.listening, name=",help"))

# async def node_connect():
#     await bot.wait_until_ready()

# @bot.event
# async def on_command_error(ctx: commands.Context, error):
#     if isinstance(error, commands.MissingRequiredArgument):
#         await ctx.send(embed=nextcord.Embed(description="missing *arguments..*", color=ctx.author.color))

# @bot.event
# async def on_command_error(ctx: commands.Context, error):
#     if isinstance(error, commands.CommandOnCooldown):
#         em = nextcord.Embed(description=f'**cooldown active**\ntry again in *{error.retry_after:.2f}s*',color=ctx.author.color)
#         await ctx.send(embed=em)

bot.run(YOUR_BOT_TOKEN)
if __name__ == '__main__':
    pass
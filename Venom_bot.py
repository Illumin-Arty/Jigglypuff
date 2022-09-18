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

# PATH_OF_DIRSONGS = os.getenv('DIRSONGS')

@bot.event
async def on_ready():

    PATH_OF_DIRSONGS = input('Input Folder: ')

    if PATH_OF_DIRSONGS == None :
        PATH_OF_DIRSONGS = os.getenv('DIRSONGS')
        # PATH_OF_DIRSONGS = f'{os.getcwd()}\\songs\\'
    # print(PATH_OF_DIRSONGS)
    # return

    guild = nextcord.utils.get(bot.guilds, id=YOUR_GUILD_ID)

    voice_channel: nextcord.VoiceChannel = nextcord.utils.get(guild.voice_channels, id=YOUR_CHANNEL_ID)

    class Queue(list):
        def __init__(self, names, voice):
            super(Queue, self).__init__(names)
            self.voice = voice
            self.pos = 0
            self.max = len(names) - 1

        def play(self):
            self.voice.play(nextcord.FFmpegPCMAudio(source=self[self.pos]), after=self.manager)
            now = time.localtime(time.time())
            print(f'({now.tm_hour:02}:{now.tm_min:02}:{now.tm_sec:02}) Track no. {self.pos} is launched without any problem!')

        def manager(self, err=None):
            if err:
                print(err)
            if self.pos == self.max:
                self.pos = 0
            else:
                self.pos += 1

            self.play()

    async def main():
        if voice_channel != None:
            vc: nextcord.VoiceClient = await voice_channel.connect()

            song_list = []
            counter = 0
            for file in pathlib.Path(PATH_OF_DIRSONGS).iterdir():
                print(file)
                song_list.append(file)
                print(song_list)
                counter += 1 
                if counter == 2 :
                    break



            _Queue = Queue(song_list, vc)

            _Queue.play()

        else:
            print("Error!")

    await main()
    print("The bot is launched the music will start!")



bot.run(YOUR_BOT_TOKEN)
if __name__ == '__main__':
    pass

import discord
from discord.ext import commands
from colorama import Fore, init



# At the start of the selfbot :
bot = commands.Bot(self_bot=True, help_command=None, command_prefix='!')


@bot.event
async def on_ready():
    init()
    print(Fore.RED + """
 ██████╗██████╗ ██╗███╗   ██╗ ██████╗ ███████╗    ███████╗███████╗██╗     ███████╗██████╗  ██████╗ ████████╗
██╔════╝██╔══██╗██║████╗  ██║██╔════╝ ██╔════╝    ██╔════╝██╔════╝██║     ██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝
██║     ██████╔╝██║██╔██╗ ██║██║  ███╗█████╗      ███████╗█████╗  ██║     █████╗  ██████╔╝██║   ██║   ██║   
██║     ██╔══██╗██║██║╚██╗██║██║   ██║██╔══╝      ╚════██║██╔══╝  ██║     ██╔══╝  ██╔══██╗██║   ██║   ██║   
╚██████╗██║  ██║██║██║ ╚████║╚██████╔╝███████╗    ███████║███████╗███████╗██║     ██████╔╝╚██████╔╝   ██║   
 ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝    ╚══════╝╚══════╝╚══════╝╚═╝     ╚═════╝  ╚═════╝    ╚═╝   
                                        ************************
                                        * Welcome dear Cringer *
                                        * Status : Ready       *
                                        ************************                     
                                        """)
                                                                                                            

# The Code of the "Cringe" Selfbot :

@bot.event
async def on_message(message):
    if "quoi" in message.content:
        await message.reply('feur')
    if "oui" in message.content:
        await message.reply('stiti')
    if "ouais" in message.content:
        await message.reply("stern")
    if "non" in message.content:
        await message.reply("bril")
    if "re" in message.content:
        await message.reply("nard")
    if "ah" in message.content:
        await message.reply("beille")

# And Finally the bot is running

bot.run("TOKEN", bot=False)

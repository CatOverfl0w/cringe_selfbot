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
    print(Fore.GREEN + "[LOGS]" + message.content)   
    if message.content == "quoi":
        await message.reply('feur')
    if message.content == "oui":
        await message.reply('stiti')
    if message.content == "ouais":
        await message.reply("stern")
    if message.content == "non":
        await message.reply("bril")
    if message.content == "re":
        await message.reply("nard")
    if message.content == "ah":
        await message.reply("beille")

# And Finally the bot is running

bot.run("TOKEN", bot=False)

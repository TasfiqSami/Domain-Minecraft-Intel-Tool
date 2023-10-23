from json import load
import discord
import logging

import threading
from utils.messages.messages import get_message

from utils.commands.uuid.uuid import player
from utils.commands.domain2IPConverter.domain2IPConverter import convertDomain
from utils.commands.ipInfo.ipInfo import ipInfo
from utils.commands.help.help import help
from utils.commands.support.support import support
from utils.commands.dumpedIPs.getip import getip
from utils.commands.server.returnData import getServerData

logging.basicConfig(format='[%(asctime)s] - [%(levelname)s] - %(message)s', 
                    level=logging.INFO)

LOGGER = logging.getLogger()

print(discord.Intents.all())
intents = discord.Intents(discord.Intents.all())


with open('config.json', 'r')as configFile:
    config = load(configFile)
    quboCMD = config['quboCMD']
    BOT_TOKEN = config['BOT_TOKEN']

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = discord.Client(intents=intents)


@bot.event
async def on_ready():
    global botUserName, botDiscriminator, botID
    botUserName = bot.user.name
    botDiscriminator = bot.user.discriminator
    botID = bot.user.id
    LOGGER.info(f'Bot started with username {botUserName}#{botDiscriminator}, id:{botID}')

@bot.event 
async def on_message(message):
    if message.author.id == botID:
        return
    LOGGER.info(f'Message sent in {message.channel} by {message.author}. The message was \'{message.content}\'')

    if message.content.startswith('!player '):
        try:
            _, playername = message.content.split(' ')
        except:
            await message.channel.send(get_message('command.player'))    
        await message.channel.send(f'''```{player(playername)}```''')

    if message.content.startswith('!domain '):
        try:
            _, domain = message.content.split(' ')
        except:
            await message.channel.send(get_message('command.domain'))            
        await message.channel.send(f''' {convertDomain(domain)} ''')
    
    if message.content.startswith('!ipinfo '):
        try:
            _, ip = message.content.split(' ')
        except:
            await message.channel.send(get_message('command.ipinfo'))            
        await message.channel.send(f''' {ipInfo(ip)}''')

    if message.content.startswith('!help'):        
        await message.channel.send(f''' {help()} ''')

    if message.content.startswith('!support'):        
        await message.channel.send(f''' {support()} ''')


    if message.content.startswith('!server '):
        try:
            _, domain = message.content.split(' ')
        except:
            await message.channel.send(get_message('command.server'))   
        data = getServerData(domain)
        
        motd,version,protocal,players = data
        await message.channel.send(f''' ``` {motd}\n {version}\n {protocal}\n {players}\n```''')

    if message.content.startswith('!ipget '):
        try:
            _, username = message.content.split(' ')
        except:
            await message.channel.send(get_message('command.ipget'))            
        await message.channel.send(f''' {getip(username)}''')


bot.run(BOT_TOKEN)
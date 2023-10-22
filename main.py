from json import load
import discord
import logging

from utils.commands.uuid.getPlayerUUID import player_uuid
from utils.commands.domain2IPConverter.domain2IPConverter import convertDomain
from utils.commands.ipInfo.ipInfo import ipInfo
from utils.commands.help.help import help
from utils.commands.support.support import support
from utils.commands.server.returnData import getServerData

logging.basicConfig(format='[%(asctime)s] - [%(levelname)s] - %(message)s', 
                    level=logging.INFO)

mainLogger = logging.getLogger()

intents = discord.Intents(32767)


with open('config.json', 'r')as configFile:
    config = load(configFile)
    quboCMD = config['quboCMD']
    botToken = config['botToken']

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
    mainLogger.info(f'Bot started with username {botUserName}#{botDiscriminator}, id:{botID}')


@bot.event 
async def on_message(message):
    mainLogger.info(f'Message sent in {message.channel} by {message.id}. The message was \'{message.content}\'')
    if message.author.id == botID:
        return

    # if message.content.startswith('!'):
    #     await message.channel.send('Commands are only available in commands channel')
    #     return

    if message.content.startswith('!player '):
        try:
            _, playername = message.content.split(' ')
        except Exception as e:
            await message.channel.send('```The given playername contains a space. Spaces in playernames are not allowed!``` ')    
        await message.channel.send(f'''```{player_uuid(playername)}```''')

    if message.content.startswith('!domain '):
        try:
            _, domain = message.content.split(' ')
        except Exception as e:
            await message.channel.send('```The given domain contains a space. Spaces in domains are not allowed!``` ')            
        await message.channel.send(f''' {convertDomain(domain)} ''')
    
    if message.content.startswith('!ipinfo '):
        try:
            _, ip = message.content.split(' ')
        except Exception as e:
            await message.channel.send('```The given ip is inavlid!``` ')            
        await message.channel.send(f''' {ipInfo(ip)}''')

    if message.content.startswith('!help'):        
        await message.channel.send(f''' {help()} ''')

    if message.content.startswith('!support'):        
        await message.channel.send(f''' {support()} ''')


    if message.content.startswith('!server '):
        try:
            _, domain = message.content.split(' ')
        except:
            await message.channel.send('```The given domain contains a space. Spaces in domains are not allowed!``` ')   
        data = getServerData(domain)
        
        motd,version,protocal,players = data
        await message.channel.send(f''' ``` {motd}\n {version}\n {protocal}\n {players}\n```''')
        


bot.run(botToken)
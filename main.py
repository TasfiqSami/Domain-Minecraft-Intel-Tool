from json import load
import discord
import logging

import threading
from utils.messages.messages import get_message
from utils.commands.command_parser import parse_command

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

with open('config.json', 'r') as configFile:
    config = load(configFile)
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

    LOGGER.info(f"Message sent in {message.channel} by {message.author}. The message was '{message.content}'")

    command, argument = parse_command(message.content)

    if command == "!player":
        if argument is None:
            await message.channel.send(get_message('command.player'))
            return
        await message.channel.send(f'''```{player(argument)}```''')

    elif command == "!domain":
        if argument is None:
            await message.channel.send(get_message('command.domain'))
            return
        await message.channel.send(f''' {convertDomain(argument)} ''')

    elif command == "!ipinfo":
        if argument is None:
            await message.channel.send(get_message('command.ipinfo'))
            return
        await message.channel.send(f''' {ipInfo(argument)}''')

    elif command == "!help" and argument is None:
        await message.channel.send(f''' {help()} ''')

    elif command == "!support" and argument is None:
        await message.channel.send(f''' {support()} ''')

    elif command == "!server":
        if argument is None:
            await message.channel.send(get_message('command.server'))
            return
        data = getServerData(argument)
        motd, version, protocol, players = data
        await message.channel.send(f''' ``` {motd}\n {version}\n {protocol}\n {players}\n```''')

    elif command == "!ipget":
        if argument is None:
            await message.channel.send(get_message('command.ipget'))
            return
        await message.channel.send(f''' {getip(argument)}''')


bot.run(BOT_TOKEN)

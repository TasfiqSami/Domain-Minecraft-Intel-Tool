import json

messages = {
    "command.player": "```The given playername contains a space. Spaces in playernames are not allowed!``` ",
    "command.domain": "```The given domain contains a space. Spaces in domain are not allowed!``` ",
    "command.ipinfo": "```The given ip is inavlid!``` ",
    "command.server": "```The given domain contains a space. Spaces in domains are not allowed!``` ",
    "command.ipget": "```The given username is invalid``` ",
    "command.ipget.protectedlist": "```I am sorry but I cannot provide you his/her IP```"
}
def get_message(message):return messages[message]
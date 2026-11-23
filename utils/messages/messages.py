messages = {
    "command.player": "Usage: !player <playername> (provide exactly one username without spaces).",
    "command.domain": "Usage: !domain <domain> (provide exactly one domain).",
    "command.ipinfo": "Usage: !ipinfo <ip> (provide exactly one IP address).",
    "command.server": "Usage: !server <domain> (provide exactly one server address).",
    "command.ipget": "Usage: !ipget <username> (provide exactly one username).",
    "command.ipget.protectedlist": "I am sorry but I cannot provide you his/her IP"
}


def get_message(message):
    return messages[message]

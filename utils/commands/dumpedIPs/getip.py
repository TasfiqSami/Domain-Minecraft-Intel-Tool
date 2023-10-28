import json
from utils.messages.messages import get_message
protectedlist = ['Tasfiq', 'Farazi106', 'Mikthegmr', 'SathvikGamingYT', 'asg65rip', 'zBe4tTMe', 'FAHIM678', 'woah_noicee', 'MrUniqueXD']
servers = ["China", "CrownMC", "QrexPvP"]

ips = []
def getip(username):
    ips = []
    text = ''
    if username in protectedlist: return get_message('command.ipget.protectedlist')
    for server in servers:
        with open(f'utils/{server}.json', 'r') as f:
            data = f.read()
            data = json.loads(data)    
        try: ips.append(f'IP of {username} is {data[username]} and was found in {server}') 
        except: continue
    for ip in ips: text = text + ip + '\n'
    if text == '': text = f'IP of {username} cannot be found'
    return text
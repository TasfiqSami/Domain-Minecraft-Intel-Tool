from utils.commands.server.serverData import mcstatus



def getServerData(ip, bot_output=False):

    data = mcstatus(server=ip, remove_spaces=True)
    print(data)
    if data[0] is not None:
        motd = (f'[MOTD] {data[0]}')
    version = (f'[Version] {data[1]}')


    protocal = (f'[Protocol] {data[2]}')
    players = (f'[Players] {data[3]}/{data[4]}')
    try:
        mods = (f'[Mods] {data[10]}')
    except: 
        mods = (f'[Mods] None')
    return motd, version, protocal, players

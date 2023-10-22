import requests
import hashlib
import uuid

from json import JSONDecodeError


def player_uuid(username):

    api = 'https://api.mojang.com/users/profiles/minecraft/'

    try:
        r = requests.get(f'{api}{username}')
        r_json = r.json()

        onlineUUID = r_json['id']
        onlineUUID = f'{onlineUUID[0:8]}-{onlineUUID[8:12]}-{onlineUUID[12:16]}-{onlineUUID[16:20]}-{onlineUUID[20:32]}'
        offlineUUID = str(uuid.UUID(bytes=hashlib.md5(bytes(f'OfflinePlayer:{username}', 'utf-8')).digest()[:16], version=3))
        
    except (JSONDecodeError, KeyError):
        offlineUUID = str(uuid.UUID(bytes=hashlib.md5(bytes(f'OfflinePlayer:{username}', 'utf-8')).digest()[:16], version=3))
        onlineUUID = None

    return f'''{"The player does not have a premium account" 
                                           if onlineUUID == None 
                                           else f"Premium UUID is {onlineUUID}"} 
                                           \nCracked UUID for player is {offlineUUID}'''

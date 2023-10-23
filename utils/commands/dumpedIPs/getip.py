import json
whitelist = ['Tasfiq', 'Farazi106', 'Mikthegmr', 'SathvikGamingYT', 'asg65rip']
def getip(username):
    if username in whitelist: return 'User is whitlisted'
    with open('utils/ips.json', 'r') as f:
        data = f.read()
        data = json.loads(data)
    try: return data[username] 
    except: return None

from socket import gethostbyname
def convertDomain(domain:str):
    return f"Real IP of that domain is **»** **__```{gethostbyname(domain)}```__**"
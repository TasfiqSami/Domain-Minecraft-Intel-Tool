import requests
from utils.commands.domain2IPConverter.domain2IPConverter import convertDomain
def ipInfo(ipAddr):

    try:
        r = requests.get(f'http://ip-api.com/json/{ipAddr}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,isp,org,as,query')
        r_json = r.json()

        # If the request is valid.
        if r_json['status'] == 'success':
            continent = r_json['continent']
            continent_code = r_json['continentCode']
            country = r_json['country']
            country_code = r_json['countryCode']
            region = r_json['region']
            region_name = r_json['regionName']
            city = r_json['city']

            isp = r_json['isp']
            org = r_json['org']
            as_ = r_json['as']


            return(f'''
                    Continent: {continent} Continent Code: {continent_code}
                    Country: {country} CountryCode: {country_code}
                    Region: {region}Region Name: {region_name}
                    City: {city}
                    ISP: {isp} Org: {org}
                    IP: {convertDomain(ipAddr)}
                    ''')

        else:
            return(f'Invalid ip')
        
    except requests.exceptions.ConnectionError:
        return(f'ConnectionError Please talk to server admins.')


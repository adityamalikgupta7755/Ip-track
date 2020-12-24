import requests

# request for ip
address = requests.get('https://get.geojs.io/v1/ip.json')
# fetch ip from json data
ipaddress = address.json()['ip']


urls ='https://get.geojs.io/v1/ip/geo/'
url =urls+ipaddress+'.json'

# request for data 
geo =requests.get(url)
geodata = geo.json()

# fetch data and print
print("Network Service Provider Name:-",geodata['organization_name'])
print("Longitude:-",geodata['longitude'])
print("latitude:-",geodata['latitude'])
print("Continent code:-",geodata['continent_code'])
print("Time zone:-",geodata['timezone'])
print("Country:-",geodata['country'])
print("Country code:-",geodata['country_code3'])
print("Region:-",geodata['region'])
print("City:-",geodata['city'])
print("area code:-",geodata['area_code'])
print("IP address:-",geodata['ip'])


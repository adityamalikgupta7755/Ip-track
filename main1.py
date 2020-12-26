import requests

# request for ip to api.ipify.org
address = requests.get('https://api.ipify.org?format=json')

# fetch ip from json data
ipaddress = address.json()['ip']
print("Your public ip :- ",ipaddress)


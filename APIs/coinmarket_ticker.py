import json
import requests

turl = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

request = requests.get(turl, headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'YOUR_API_KEY'
},params = {'convert':'INR'})

results = request.json()
data = results['data']

for currency in data:
    id = currency['id']
    name = currency['name']
    symbol = currency['symbol']

    price = currency['quote']['INR']['price']

    print(str(id)+' | '+name+'('+symbol+(')'))
    print()
    print('Price : RS '+str(price))
    print()
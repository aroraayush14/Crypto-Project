#Importing python modules
import json
import requests
#Storing the url in a variable
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
#User input for symbol search
sy = input('Enter Symbol:')
sy = sy.lower()
parameters = {
    'symbol':sy,
    'convert':'USD'
}

request = requests.get(url, headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'dc139d27-6afa-4ebb-9bf2-3c39229faf40',
} ,params = parameters)

results = request.json()
data = results['data']

print(json.dumps(results, sort_keys=True, indent=4))

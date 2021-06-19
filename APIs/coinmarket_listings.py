import json
import requests

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

request = requests.get(url, headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'YOUR_API_KEY',
})
results = request.json()

print(json.dumps(results, sort_keys=True, indent=4))
import json
import requests


url = 'https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest' 

request = requests.get(url, headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'YOUR_API_KEY',
})
results = request.json()

print(json.dumps(results, sort_keys=True, indent=4))

active_currency = results['data']['active_cryptocurrencies']
active_market = results['data']['active_market_pairs']
global_volume = results['data']['quote']['USD']['total_volume_24h']

print()
print('The active cryptocurrenices are '+ str(active_currency)+' Active Markets are',active_market)
print()
print('Global Volume in last 24 hours',global_volume)
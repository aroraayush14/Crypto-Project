import os
import json
from requests import Request, Session

listings_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'dc139d27-6afa-4ebb-9bf2-3c39229faf40'
}
parameters={
    'convert':'INR'
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(listings_url, params=parameters)
    res = json.loads(response.text)
    
except (ConnectionError, TimeoutError) as e:
    print(e)

data = res['data']
data[0]


ticker_url_pairs = {}
for currency in data:
    symbol = currency['symbol']
    url = currency['id']
    ticker_url_pairs[symbol] = url

print()
print('Alert Tracking')
print()

already_hit_symbols = []
convert = 'INR'
while True:
    with open('alert.txt') as inp:
        for line in inp:
            ticker, amount = line.split()
            ticker = ticker.upper()
            for i in range(len(data)):
                if data[i]['symbol'] == ticker:
                    currency = data[i]
                    rank = currency['cmc_rank']
                    name = currency['name']
                    last_updated = currency['last_updated']
                    symbol = currency['symbol']
                    quotes = currency['quote'][convert]
                    hour_change = quotes['percent_change_1h']
                    day_change = quotes['percent_change_24h']
                    week_change = quotes['percent_change_7d']
                    price = quotes['price']

                    if float(price) >= float(amount) and symbol not in already_hit_symbols:
                        os.System('say ' + name + 'hit ' + amount)
                        last_updated_string =  str(last_updated.split('T'))
                        print(name + 'hit ' + amount + 'on ' + last_updated_string)
                        already_hit_symbol.append(symbol)
print('...')
time.sleep(300)
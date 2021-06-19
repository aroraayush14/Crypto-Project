import math
import json
from requests import Request, Session
from prettytable import PrettyTable
 
global_url = 'https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest'

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'YOUR_API_KEY'
}
parameters={
    'convert':'INR'
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(global_url, params=parameters)
    res = json.loads(response.text)
    
except (ConnectionError, TimeoutError) as e:
    print(e)

data = res['data']
data
global_cap = data['quote']['INR']['total_market_cap']

table = PrettyTable(['Name', 'Ticker', '% of total global cap', 'Current', '10.9T (Gold)', '35.2T (Narrow Money)', '89.5T (World Stock Markets)', '95.7T (Broad Money)', '280T (Real Estate)', '558T (Derivatives)'])
 
listings_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'dc139d27-6afa-4ebb-9bf2-3c39229faf40'
}
parameters={
        'limit':'100', 'convert':'INR',
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
   

for currency in data:
    name = currency['name']
    symbol = currency['symbol']
        
 

 
    percentage_of_global_cap = float(currency['quote']['INR']['market_cap']) / float(global_cap)
    current_price = round(float(currency['quote']['INR']['price']),2)
    available_supply = float(currency['total_supply'])
    
    trillion10price = round(10900000000000 * percentage_of_global_cap / available_supply,2)
    trillion35price = round(35000000000000 * percentage_of_global_cap / available_supply,2)
    trillion73price = round(89500000000000 * percentage_of_global_cap / available_supply,2)
    trillion95price = round(95700000000000 * percentage_of_global_cap / available_supply,2)
    trillion280price = round(280000000000000 * percentage_of_global_cap / available_supply,2)
    trillion558price = round(558000000000000 * percentage_of_global_cap / available_supply,2)
    
    percentage_of_global_cap_string = str(round(percentage_of_global_cap*100,2)) + '%'
    
    current_price_string = '₹ ' + str(current_price)
    
    trillion10price_string = '₹ ' + '{:,}'.format(trillion10price)
    trillion35price_string = '₹ ' + '{:,}'.format(trillion35price)
    trillion73price_string = '₹ ' + '{:,}'.format(trillion73price)
    trillion95price_string = '₹ ' + '{:,}'.format(trillion95price)
    trillion280price_string = '₹ ' + '{:,}'.format(trillion280price)
    trillion558price_string = '₹ ' + '{:,}'.format(trillion558price)
    
    table.add_row([name,
                symbol,
                percentage_of_global_cap_string,
                current_price_string,
                trillion10price_string,
                trillion35price_string,
                trillion73price_string,
                trillion95price_string,
                trillion280price_string,
                trillion558price_string])
print()
print(table)
print()
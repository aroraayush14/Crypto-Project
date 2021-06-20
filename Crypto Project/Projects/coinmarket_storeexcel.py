import xlsxwriter
from requests import Request, Session
import json

start = 1
f = 1

crypto_workbook = xlsxwriter.Workbook('show.xlsx')
crypto_sheet = crypto_workbook.add_worksheet()

crypto_sheet.write('A1', 'Name')
crypto_sheet.write('B1', 'Symbol')
crypto_sheet.write('C1', 'Market Cap')
crypto_sheet.write('D1', 'Price')
crypto_sheet.write('E1', '24H Volume')
crypto_sheet.write('F1', 'Hour Change')
crypto_sheet.write('G1', 'Dsay Change')
crypto_sheet.write('H1', 'Week Change')

listings_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'YOUR_API_KEY'
}
parameters={ 'start':'1',
    'limit':'500',
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

for currency in data:
        rank = currency['cmc_rank']
        name = currency['name']
        last_updated = currency['last_updated']
        symbol = currency['symbol']
        quotes = currency['quote']['INR']
        market_cap = quotes['market_cap']
        hour_change = quotes['percent_change_1h']
        day_change = quotes['percent_change_24h']
        week_change = quotes['percent_change_7d']
        price = quotes['price']
        volume = quotes['volume_24h']

        crypto_sheet.write(f,0,name)
        crypto_sheet.write(f,1,symbol)
        crypto_sheet.write(f,2,str(market_cap))
        crypto_sheet.write(f,3,str(price))
        crypto_sheet.write(f,4,str(volume))
        crypto_sheet.write(f,5,str(hour_change))
        crypto_sheet.write(f,6,str(day_change))
        crypto_sheet.write(f,7,str(week_change))
        
        f += 1

crypto_workbook.close()
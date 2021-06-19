import os
import json
from requests import Request, Session
from prettytable import PrettyTable
from colorama import Fore, Fore, Style

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
#print(ticker_url_pairs)
print()
print('My Portfolio')
print('--------------')
print()

portfolio_value = 0.00
convert = 'INR'
last_updated = 0

table = PrettyTable(['Asset','Amount Owned', 'INR Value','Price','1h','24h','7d'])

with open('portfolio.txt') as inp:
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


        value = float(price) * float(amount)
        

        if hour_change > 0:

            hour_change = Fore.GREEN + str(hour_change) + '%' + Style.RESET_ALL
        else:
            hour_change = Fore.RED + str(hour_change) + '%' + Style.RESET_ALL

        if day_change > 0:
            day_change = Fore.GREEN + str(day_change) + '%' + Style.RESET_ALL
        else:
            day_change = Fore.RED + str(day_change) + '%' + Style.RESET_ALL

        if week_change > 0:
            week_change = Fore.GREEN + str(week_change) + '%' + Style.RESET_ALL
        else:
            week_change = Fore.RED + str(week_change) + '%' + Style.RESET_ALL

        portfolio_value += value

        value_string = '{:,}'.format(round(value,2))

        table.add_row([name + '(' + symbol + ')',
        amount,
        '₹ ' + value_string,
        '₹ ' + str(price),
        str(hour_change),
        str(day_change),
        str(week_change)])

print(table)
print()

portfolio_value_string = '{:,}'.format(round(portfolio_value,2))
last_updated_string =  str(last_updated.split('T'))

print('Total Portfolio Value : ' + Fore.GREEN + '₹' + portfolio_value_string + Style.RESET_ALL)
print()
print('API Results Last Updated on : ' + last_updated_string + Style.RESET_ALL)
print()
        
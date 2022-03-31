import os
import json
from requests import Request, Session
from prettytable import PrettyTable
from colorama import Fore, Fore, Style, Back

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

choice = input('Enter slug:')
choice = choice.upper()
table = PrettyTable(['Asset','Price','1h','24h','7d'])
if choice in ticker_url_pairs:
        for i in range(len(data)):
            if data[i]['symbol'] == choice:
                currency = data[i]
                rank = currency['cmc_rank']
                name = currency['name']
                last_updated = currency['last_updated']
                symbol = currency['symbol']
                quotes = currency['quote']['INR']
                hour_change = quotes['percent_change_1h']
                day_change = quotes['percent_change_24h']
                week_change = quotes['percent_change_7d']
                price = quotes['price']



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

                table.add_row([name + '(' + symbol + ')',
                '₹ ' + str(price),
                str(hour_change),
                str(day_change),
                 str(week_change)])

print()
print('Ticker: '+ choice)
print('--------------')
print()


print(table)

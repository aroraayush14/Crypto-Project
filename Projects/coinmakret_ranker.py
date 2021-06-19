import os
import json
from requests import Request, Session
from prettytable import PrettyTable
from colorama import Fore, Fore, Style

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

global_cap = data['quote']['INR']['total_market_cap']
global_cap_string = '{:,}'.format(global_cap)



while True:
    print()
    print('Explorer Menu')
    print('--------------')
    print()
    print('The Global market cap is ₹ '+ global_cap_string)
    print()
    print('1 - Top 100 sorted by Name')
    print('2 - Top 100 sorted by 24 Hour Change')
    print('3 - Top 100 sorted by 24 Hour Volume')
    print('0 - Exit')
    print()
    choice = input('Enter your Choice - ')
    
    if choice == '1':
        sot = 'name'
    if choice == '2':
        sot = 'percent_change_24h'
    if choice == '3':
        sot = 'volume_24h'
    if choice == '0':
        break

    listings_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'dc139d27-6afa-4ebb-9bf2-3c39229faf40'
    }
    parameters={
        'limit':'100', 'convert':'INR','sort':sot
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
    table = PrettyTable(['Rank','Asset','Price','Market Cap','Volume','1h','24h','7d'])
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


        if hour_change is not None:
            if hour_change > 0:
                hour_change = Fore.GREEN + str(hour_change) + '%' + Style.RESET_ALL
            else:
                hour_change = Fore.RED + str(hour_change) + '%' + Style.RESET_ALL
        if day_change is not None:
            if day_change > 0:
                day_change = Fore.GREEN + str(day_change) + '%' + Style.RESET_ALL
            else:
                day_change = Fore.RED + str(day_change) + '%' + Style.RESET_ALL
        if week_change is not None:
            if week_change > 0:
                week_change = Fore.GREEN + str(week_change) + '%' + Style.RESET_ALL
            else:
                week_change = Fore.RED + str(week_change) + '%' + Style.RESET_ALL

        if volume is not None:
            volume_string = '{:,}'.format(volume)
        if market_cap is not None:
            volume_string = '{:,}'.format(market_cap)
        

        table.add_row([rank, name + '(' + symbol + ')',
        '₹ ' + str(price),
        '₹ ' + str(market_cap),
        '₹ ' + volume_string,
        str(hour_change),
        str(day_change),
        str(week_change)])

    print()
    print(table)
    print()

    choice1 = input('Again? (y/n):')

    if choice1 == 'n':
    
        break
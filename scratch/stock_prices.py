import os
import yfinance as yf
import datetime
from time import sleep

os.chdir('/home/r3dux/code/python/projects/stock_tools/check_price/')



# HEADER DISPLAY
def display():
    os.system('clear')
    os.system('figlet -f mini "S T O C K  P R I C E S" | boxes -d simple')
    print("\n")



# GET CURRENT STOCK PRICE
def get_current_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')

    return todays_data['Close'][0]
    


# COMPARE TODAY AND YESTERDAY'S PRICES
def get_day_price(symbol):
    ticker = yf.Ticker(symbol)

    # WHOLE DAY DATA SET
    todays_data = ticker.history(period='1d')
    yesterdays_data = ticker.history(period='2d')

    # PRICE AT CLOSE
    todays_price = todays_data['Close'][0]
    yesterdays_price = yesterdays_data['Close'][0]
    
    print(f'{"    "}[{symbol.upper()}]\n')
    print(f'{"    "}{"TODAY:":<12} ${"%.2f"%todays_price}')
    print(f'{"    "}{"YESTERDAY:":<12} ${"%.2f"%yesterdays_price}')

    # PRICE CHANGE SINCE YESTERDAY
    def price_change(today, yesterday):
        diff = todays_price - yesterdays_price
        average = (todays_price + yesterdays_price)/2
        percentage_diff = diff / average * 100
        percentage_diff = "%.2f" % percentage_diff
        return percentage_diff

    if float(todays_price) > float(yesterdays_price):
        print(f'{"    "}{"CHANGE:":<12} +{price_change(todays_price, yesterdays_price)}%\n')
        print('    Price up since yesterday!')
    elif todays_price < yesterdays_price:
        print(f'{"    "}{"CHANGE:":<12} {price_change(todays_price, yesterdays_price)}%\n')
        print('    Price down since yesterday')
    else:
        print(f'{"    "}{"CHANGE:":<12} {price_change(todays_price, yesterdays_price)}%')
        print('    Price is the same as yesterday!!!')



def get_watchlist():
    watchlist = {}
    print('    [ WATCHLIST ]    ')
    with open ('./watchlist.txt', 'r') as wl:
        for line in wl:
            line = str(line).replace('\n', '')

            get_price = "%.2f" % get_current_price(line)

            ticker = f'{line.upper()}'
            price = f'{get_price}'

            watchlist[ticker] = price
    print('\n')
    for ticker, price in watchlist.items():
        print(f'{"    "}{ticker:<12} ${price}')
    print('\n')



def main():
    display()
    get_watchlist()
    stock = input("ENTER TICKER SYMBOL: ")
    print('\n')
    get_day_price(stock)



main()

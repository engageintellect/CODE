import os
import yfinance as yf
import datetime
from time import sleep


os.chdir('/home/r3dux/code/python/projects/stock_tools/check_price')


# HEADER DISPLAY
def display():
    os.system('clear')
    os.system('figlet -f mini "S T O C K  P R I C E S" | boxes -d simple')
    print("\n")



def get_current_price(symbol):
    ticker = yf.Ticker(symbol)

    # WHOLE DAY DATA SET
    todays_data = ticker.history(period='1d')
    yesterdays_data = ticker.history(period='2d')

    # PRICE AT CLOSE
    todays_price = todays_data['Close'][0]
    yesterdays_price = yesterdays_data['Close'][0]

    
    # return todays_data['Close'][0]       
    print(f'TODAY:{todays_price}')
    # print(f'YESTERDAY:{yesterdays_price}')

    


    # PRICE CHANGE SINCE YESTERDAY
    def price_change(today, yesterday):
        diff = todays_price - yesterdays_price
        average = (todays_price + yesterdays_price)/2
        percentage_diff = diff / average * 100
        percentage_diff = "%.2f" % percentage_diff
        return percentage_diff
    
    if todays_price > yesterdays_price:
        print('Price up since yesterday!')
        print(f'+{price_change(todays_price, yesterdays_price)}%')
    elif todays_price < yesterdays_price:
        print('Price down since yesterday')
        print(f'{price_change(todays_price, yesterdays_price)}%')
    else:
        print('Price is the same as yesterday!!!')
        print(f'{price_change(todays_price, yesterdays_price)}%')



def get_watchlist():
    watchlist = {}
    print('    [ WATCHLIST ]     ')
    with open ('./watchlist.txt', 'r') as wl:
        for line in wl:
            line = str(line).replace('\n', '')
            
            get_price = "%.2f" % get_current_price(line)
            # get_price = get_current_price(line)

            ticker = f'{line.upper()}'
            price = f'{get_price}'

            watchlist[ticker] = price

    print('\n')
    for ticker, price in watchlist.items():
        print(f'{"    "}{ticker:<8} ${price}')
    print('\n')



def main():
    # display()
    # get_watchlist()
    # stock = input("ENTER TICKER SYMBOL: ")
    print(get_current_price('GME'))

main()

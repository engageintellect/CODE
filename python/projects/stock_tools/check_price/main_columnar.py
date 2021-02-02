import os
import yfinance as yf
import datetime
from time import sleep
from columnar import columnar

os.chdir('/home/r3dux/code/python/projects/stock_tools/check_price')


def display():
    os.system('clear')
    os.system('figlet -f mini "S T O C K   P R I C E S" | boxes -d simple')
    print("\n")


def get_current_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return todays_data['Close'][0]


def get_watchlist():
    headers = ["STOCK", "PRICE"]
    watchlist = []
    
    print('   [ WATCHLIST ]   ')
    with open ('./watchlist.txt', 'r') as wl:
        for line in wl:
            line = str(line).replace('\n', '')
            get_price = "%.2f" % get_current_price(line)
            ticker = f'{line.upper()}'
            price = f'{get_price}'
            ticker = [ticker, price]
            watchlist.append(ticker)

    table = columnar(watchlist, headers, no_borders=True, min_column_width=10)
    print(table)
    print('\n')

    # print(watchlist)


def main():
    display()
    get_watchlist()
    stock = input("ENTER TICKER SYMBOL: ")
    # display()
    price = "%.2f" % get_current_price(stock)
    print(f'{stock.upper()} = [${price}]')
    sleep(3)
    main()

main()

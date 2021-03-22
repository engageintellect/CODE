#!/usr/bin/env python3
import os
import subprocess
import yfinance as yf
import datetime
from time import sleep
from columnar import columnar


os.chdir('/home/r3dux/code/python/projects/stock_tools/check_price/')

def display():
    os.system('clear')
    os.system('figlet -f mini "STOCK PRICES" | boxes -d simple')
    print('\n')
    pass


def console():
    stock_name = input('Enter stock ticker name: ')
    if stock_name == 'q':
        os.system('clear')
        quit()

    ticker = yf.Ticker(stock_name.upper())

    today = ticker.history(period='0d')
    week = ticker.history(period='7d')
    month = ticker.history(period='30d')

    chart_size = input('Choose chart size (d,w,m): ')

    if chart_size  == 'q':
        os.system('clear')
        main()
    else:
        pass
    
    if chart_size == 'd':
        print(today)
    elif chart_size == 'w':
        print(week)
    elif chart_size == 'm':
        print(month)
    else:
        print('Please choose a correct option...')
    pass

    console()



def get_current_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')

    open_price = todays_data['Open'][0]
    close_price = todays_data['Close'][0]
    volume = todays_data['Volume'][0]


    return todays_data['Open'][0]
def watchlist():
    headers = ["STOCK", "OPEN", "CLOSE", "HIGH", "LOW", "VOLUME", "CHANGE"]
    my_watchlist = []

    with open ('./watchlist.txt', 'r') as wl:
        for line in wl:
            line = str(line).replace('\n', '')
            get_price = "%.2f" % get_current_price(line)
            ticker = f'{line.upper()}'
            price = f'{get_price}'
            ticker = [ticker,price]

            my_watchlist.append(ticker)
    table = columnar(my_watchlist, headers, no_borders=True, min_column_width=10)
    print(table)
    print('\n')

    print(open_price)


    pass

def price_action():
    pass


def main():
    display()
    watchlist()
    

main()

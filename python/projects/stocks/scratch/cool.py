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
    os.system('figlet -f mini "        S T O C K  P R I C E S" | boxes -d simple')
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

    print('\n')
    console()



def price_open(stock):
    ticker = yf.Ticker(stock)
    data = ticker.history(period='1d')
    return "%.2f" % data['Open'][0]

def price_close(stock):
    ticker = yf.Ticker(stock)
    data = ticker.history(period='1d')
    return "%.2f" % data['Close'][0]

def price_high(stock):
    ticker = yf.Ticker(stock)
    data = ticker.history(period='1d')
    return "%.2f" % data['High'][0]

def price_low(stock):
    ticker = yf.Ticker(stock)
    data = ticker.history(period='1d')
    return "%.2f" % data['Low'][0]

def volume(stock):
    ticker = yf.Ticker(stock)
    data = ticker.history(period='1d')
    return int(data['Volume'][0])



def watchlist():
    headers = ["STOCK", "OPEN", "CLOSE", "HIGH", "LOW", "VOLUME", "CHANGE"]
    my_watchlist = []

    os.chdir('/home/r3dux/code/python/projects/stock_tools/check_price')

    with open ('./watchlist.txt', 'r') as wl:
        for line in wl:
            ticker = line.replace('\n', '').upper()
            open_price = f'${price_open(ticker)}'
            low_price = f'${price_low(ticker)}'
            high_price = f'${price_high(ticker)}'
            close_price = f'${price_close(ticker)}'
            total_volume = f'{volume(ticker)}'

            ticker = [ticker, open_price, low_price, high_price, close_price, total_volume]
            my_watchlist.append(ticker)

    table = columnar(my_watchlist, headers, no_borders=True, min_column_width=10)
    print(table)
    print('\n')



def main():
    display()
    watchlist()
    console()

main()

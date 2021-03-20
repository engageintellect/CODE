#!/usr/bin/env python3
import os
import subprocess
import yfinance as yf
import datetime
from time import sleep
from columnar import columnar
import fontawesome as fa

os.chdir('/home/r3dux/code/python/projects/stock_tools/check_price/')



def display():
    os.system('clear')
    # os.system('figlet -f mini "S T O C K  P R I C E S" | boxes -d simple')
    os.system('figlet -f mini "S T O C K  P R I C E S"')
    print('\n')
    pass



def console():
    stock_name = input('SEARCH TICKER >  ')
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
    return "%.2f" % data['Low'][0]

def price_high(stock):
    ticker = yf.Ticker(stock)
    data = ticker.history(period='1d')
    return "%.2f" % data['High'][0]

def price_low(stock):
    ticker = yf.Ticker(stock)
    data = ticker.history(period='1d')
    return "%.2f" % data['Close'][0]

def volume(stock):
    ticker = yf.Ticker(stock)
    data = ticker.history(period='1d')
    return int(data['Volume'][0])

def liquidity(stock):
    ticker = yf.Ticker(stock)
    data = ticker.history(period='1d')

    first_price = data['High'][0]
    second_price = data['Low'][0]
    liquid = (second_price-first_price)*100/first_price
    l = str(liquid)
    return l[1:5]

def change(stock):
    ticker = yf.Ticker(stock)
    data = ticker.history(period='1d')
    open_price = data['Open'][0]
    close_price = data['Close'][0]

    diff = close_price - open_price
    average = (close_price + open_price)/2
    percentage_diff = diff /average * 100
    percentage_diff = "%.2f" % percentage_diff

    if float(percentage_diff) > 0:
        return f'+{percentage_diff}'
    elif float(percentage_diff) < 0:
        return f'{percentage_diff}'
    else:
        return 0

def status(stock):
    ticker = yf.Ticker(stock)
    data = ticker.history(period='1d')
    open_price = data['Open'][0]
    close_price = data['Close'][0]

    if close_price > open_price:
        return  f'     '
    elif close_price < open_price:
        return  f'     '
    else:
        return  f'     '




def watchlist():
    headers = ["[STOCK]", "[STATUS]", "[CHANGE]", "[LAST]",  "[OPEN]", "[HIGH]", "[LOW]", "[VOLUME]", "[LIQUIDITY]"]
    my_watchlist = []

    os.chdir('/home/r3dux/code/python/projects/stock_tools/check_price')

    with open ('./watchlist.txt', 'r') as wl:
        for line in wl:
            ticker = str(line.replace('\n', '').upper())
            ticker = f'{ticker}'
            open_price = f'${price_open(ticker)}'
            close_price = f'${price_close(ticker)}'
            high_price = f'${price_high(ticker)}'
            low_price = f'${price_low(ticker)}'
            total_volume = f'{volume(ticker):,}  '
            total_liquidity = f'{liquidity(ticker)}  '
            price_change = f'{change(ticker)} %'
            stock_status = f'{status(ticker)}'

            ticker = [ticker, stock_status, price_change, low_price, open_price, high_price, close_price, total_volume, total_liquidity]
            my_watchlist.append(ticker)

    table = columnar(my_watchlist, headers, no_borders=True, min_column_width=10)
    os.system('clear')
    display()
    print(table)
    print('\n')



def main():
    display()
    os.system('fortune')
    print('\n\nLOADING...')
    watchlist()
    console()
    
main()

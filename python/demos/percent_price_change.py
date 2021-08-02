import os
import subprocess
import yfinance as yf

user = subprocess.getoutput('echo $USER')
os.chdir(f'/home/{user}/code/python/projects/stock_tools/check_price')



def display():
    os.system('clear && figlet screener')
    print('\n')



def get_stock_data(stock):
    ticker = yf.Ticker(stock)
    todays_data = ticker.history(period='1d')
    
    open_price = todays_data['Open'][0]
    close_price = todays_data['Close'][0]

    diff = close_price - open_price
    average = (close_price + open_price)/2
    percentage_diff = diff / average * 100
    percentage_diff = "%.2f" % percentage_diff

    if close_price > open_price:
        print(f'{stock.upper()} IS UP\n')
        print(f'+{percentage_diff}%')
        print(f'OPEN:   ${"%.2f" % open_price}')
        print(f'CLOSE:  ${"%.2f" % close_price}')
    elif close_price < open_price:
        print(f'{stock.upper()} IS DOWN\n')
        print(f'{percentage_diff}%')
        print(f'OPEN:   ${"%.2f" % open_price}')
        print(f'CLOSE:  ${"%.2f" % close_price}')
    else:
        print(f'{stock.upper()} IS NEUTRAL\n')
        print(f'{percentage_diff}%')
        print(f'OPEN:   ${"%.2f" % open_price}')
        print(f'CLOSE:  ${"%.2f" % close_price}')

    # return open_price, close_price, percentage_diff



def get_volume(stock):
    ticker = yf.Ticker(stock)
    todays_data = ticker.history(period='1d')
    todays_volume = todays_data['Volume'][0]
    print(f'VOLUME: {todays_volume:,}')




def main():
    display()
    stock_name = str(input('ENTER STOCK TICKER: '))
    display()
    get_stock_data(stock_name)
    get_volume(stock_name)


main()

import os
import yfinance as yf
import datetime
from time import sleep


def display():
    os.system('clear')
    os.system('figlet -cf mini "S T O C K   P R I C E S"')
    print("\n")

def get_current_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return todays_data['Close'][0]


def main():
    display()
    stock = input("ENTER TICKER SYMBOL: ")
    display()
    price = "%.2f" % get_current_price(stock)
    print(f'{stock.upper()} = [${price}]')
    sleep(3)
    main()

main()

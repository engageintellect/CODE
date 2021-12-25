# coding=utf-8

import ccxt
import os


### DISPLAY ####
def display():
    os.system('clear && figlet "COINBASE"')
    print('\n')


### ACCOUNT CREDINTIALS ####
coinbase_pro = ccxt.coinbasepro({
    'apiKey': '2851606201d8765e5f91a93cd710707b',
    'secret': 'DVYqJXYxdaiinH7sTeWsTV5alpYRy2jtT/5P3xFbh96OTuDcVjdmmBKPbQMv7sWuGWQM88Ho9O/L/oIn50Ip1g==',
    'password': '5behhxfij45'
})

gemini = ccxt.gemini({
    'apiKey': 'master-bkm4AS6XfKmmctFaJ5n1',
    'secret': '3q2B8futRKUqmF53eiPf6zK7Gihz'
    # 'password': ''
})



### TRADING PAIRS ###


# trading_pairs = coinbase_pro.load_markets()

# for x in trading_pairs:
    # print(x)


# for x in coinbase_pro.id, trading_pairs:
#     print(x)


### GET PRICE ###
def fetch_ticker(ticker_name):
    ticker = gemini.fetch_ticker(f'{ticker_name}')

    print('\nSYMBOL: ', ticker['symbol'],
            '\nLAST: ', ticker['last'])

    
### BUY ###
def market_order(side, price, ticker_name, amount):
    if side == 'buy':
        print('hello', gemini.id, 'bye',  gemini.create_limit_buy_order(ticker_name, amount, price))
    elif side == 'sell':
        print(gemini.id, gemini.create_market_sell_order(ticker_name.upper(), price, amount))
    else:
        print('Incorrect entry, please try again...')
        main()








# print(coinbase_pro.id, coinbase_pro.create_market_buy_order('ETH/USD', .001))


def main():
    display()
    # ticker = input("ENTER TICKER: ").upper()
    # fetch_ticker(ticker)
    # usr_continue = input("PRESS ENTER TO CONTINUE")
    # if usr_continue != 'q':
        # main()
    # else:
        # quit()

    market_order('buy', '.001', 'ETH/USD', '2500')



main()

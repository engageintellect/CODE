#!/usr/bin/env python3

import cbpro
import datetime
import os
import requests
import time



##############################[ CLIENT ]##############################
# PUBLIC
public_client = cbpro.PublicClient()

# USER ACCOUNT
key = 'API KEY'
b64secret = 'SECRET'
passphrase = 'PASSPHRASE'
auth_client = cbpro.AuthenticatedClient(key, b64secret, passphrase)



##############################[ HOLDINGS ]##############################
holdings = {
        'usd':      'a0aed716-3988-4968-ad48-275ec367c20b',
        'usdt':     'ad065117-e2a6-4e76-8b97-9d624fa7aa4c', 
        'ada':      '9d2da30b-4a1e-4167-9ec0-94cc61845a62',
        'btc':      'ef024b07-d09d-4e14-9f46-853ad5ff198c',
        'eth':      '5fa9017e-e8f0-4fd4-b449-96cc5741a5d8',
        'doge':     'c24a49df-2c6f-414d-9109-f2dbd189a0f8', 
        'enj':      '30bd089f-83ec-41dd-974d-fddfbce1d1cf', 
        'matic':    '3d7ea903-3828-4164-bf63-b071e616c122',
        'sol':      '721596a0-4dc1-4bf2-a310-e3519b55efa6',
        'xlm':      '461ea669-ca1e-446a-bd15-f423c8bab712',
        'xrp':      'a314367f-18cb-4993-b175-7124dcac066f'
        }



##############################[ PUBLIC FUNCTIONS ]##############################

# usr_ticker = str(input("ENTER TICKER NAME: "))
# change = public_client.get_product_24hr_stats(usr_ticker)
# order_book = public_client.get_product_order_book(usr_ticker)
# ticker = public_client.get_product_ticker(usr_ticker)
# historic_rate = public_client.get_product_historic_rates(usr_ticker)
# time = auth_client.get_time()
# get_accounts = auth_client.get_accounts()
# get_currencies = auth_client.get_currencies()

def show_holdings(wallet):
    for x in auth_client.get_account(wallet):
        print(x, ': ', auth_client.get_account(wallet)[x])



##############################[ BUY & SELL ]##############################

### LIMIT ORDER

# auth_client.buy(price='100.00', #USD
#         size='0.01', #BTC
#         order_type='limit',
#         product_id='BTC-USD')
    
# auth_client.sell(price='100.00', #USD
#         size='0.01', #BTC
#         order_type='limit',
#         product_id='BTC-USD')


### MARKET ORDER

def market_order():
    display()
    print("                 BUY  ----- 1")
    print("                 SELL ----- 2\n\n")
    buy_or_sell = input("> ")

    display()
    if buy_or_sell == 'q' or buy_or_sell == '':
        os.system('clear')
        main()
    else:
        pass
    
    asset = input("CHOOSE ASSET > ")
    if asset == 'q' or asset == '':
        market_order()
    else:
        print(requests.get(f'https://rate.sx/{asset.replace("-usd","")}').text)

    if buy_or_sell == '1':
        amount = input("ENTER AMOUNT TO BUY > $")
    else:
        amount = input("ENTER AMOUNT TO SELL > $")

    if amount == 'q' or amount == '':
        market_order()
    else:
        pass
    print("\n")

    if asset == 'q' or amount == 'q':
        os.system('clear')
        main()
    elif asset == '' or amount == '':
        main()

    
    if buy_or_sell == '1':
        cmd_buy = auth_client.place_market_order(product_id=asset.upper(), side='buy', funds=amount)
        for x in cmd_buy:
            print(x, ': ', cmd_buy[x])
    elif buy_or_sell == '2':
        cmd_sell = auth_client.place_market_order(product_id=asset.upper(), side='sell', funds=amount)
        for x in cmd_sell:
            print(x, ': ', cmd_sell[x])



##############################[ DISPLAY }##############################
def display():
    os.system('clear && figlet "COINBASE PRO"')
    print('\n')



##############################[ MENU }##############################
def menu():
    print('                 MY BALANCE   ---------- 1')
    print('                 COIN INFO    ---------- 2')
    print('                 TRADE        ---------- 3')
    print('                 QUIT         ---------- q')
    print('\n\n')

    usr_input = input("> ")

    
    while usr_input != 'q':
        # BALANCE
        if usr_input == '1':
            display()
            choose_asset = input("CHOOSE ASSET > ")
            y = auth_client.get_account(holdings[f'{choose_asset}'])
            display()
            for x in y:
                print(x.upper(), ': ',  y[x])
        # SEARCH
        elif usr_input == '2':
            display()
            usr_ticker = input("ENTER ASSET > ")
            timeframe = input("ENTER TIMEFRAME > ")

            display()
            if timeframe == '':
                print(requests.get(f'https://rate.sx/{usr_ticker.replace("-usd","")}').text)
            else:
                print(requests.get(f'https://rate.sx/{usr_ticker.replace("-usd","")}@{timeframe}').text)
            change = public_client.get_product_24hr_stats(usr_ticker.upper())
            for x in change:
                print(x, ': ', change[x])
        # TRADE
        elif usr_input == '3':
            market_order()
        
        else:
            display()
            print('PLEASE ENTER A VALID CHOICE...')
            main()
        
        usr_continue = input("\n\nPRESS ENTER TO CONTINUE > ")
        if usr_continue == '':
            pass
        main()
    else:
        os.system('clear')
        quit()
        



def main():
    # get_accounts = auth_client.get_accounts()
    # for x in get_accounts:
        # print(x)
    # quit()
    display()
    menu()
main()

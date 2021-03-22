import os
import subprocess
from time import sleep



def display():
    os.system('clear')
    print("---------------------------------------")
    os.system('figlet "OPTIONS"')
    print("---------------------------------------")
    print("\n")


def call_option():
    display()
    print("===[ CALL OPTION ]===")
    stock_price =   float(input("\nCurrent stock price: "))
    strike_price =  float(input("Strike price: "))
    target_price =  float(input("Target price: "))
    premium =       float(input("Premium price: "))

    profit_per_share = float(target_price - strike_price - premium)
    potential_profit = float(profit_per_share * 100)
    profit = "%.2f" % potential_profit

    current_price =     f'CURRENT PRICE:    ${stock_price}'
    total_premium =     f'PREMIUM:          ${premium * 100}'
    break_even =        f'BREAK EVEN:       ${premium + strike_price}'
    potential_loss =    f'POTENTIAL LOSS:   ${premium * 100}'
    potential_gain =    f'POTENTIAL GAIN:   ${profit}'

    display()
    print("===[ BREAK DOWN ]===\n")
    print(current_price, "\n")
    print(total_premium)
    print(break_even)
    print(potential_loss)
    print(potential_gain)
    quit()


def put_option():
    display()
    print("===[ PUT OPTION ]===")
    stock_price =   float(input("\nCurrent stock price: "))
    strike_price =  float(input("Strike price: "))
    target_price =  float(input("Target price: "))
    premium =       float(input("Premium price: "))

    profit_per_share = float(strike_price - target_price - premium)
    potential_profit = float(profit_per_share * 100)
    profit = "%.2f" % potential_profit

    current_price =     f'CURRENT PRICE:    ${stock_price}'
    total_premium =     f'PREMIUM:          ${premium * 100}'
    break_even =        f'BREAK EVEN:       ${premium + strike_price}'
    potential_loss =    f'POTENTIAL LOSS:   ${premium * 100}'
    potential_gain =    f'POTENTIAL GAIN:   ${profit}'

    display()
    print("===[ BREAK DOWN ]===\n")
    print(current_price, "\n")
    print(total_premium)
    print(break_even)
    print(potential_loss)
    print(potential_gain)
    quit()


def debit_spread():
    pass


def menu():
    print('        1 ---------- CALL')
    print('        2 ---------- PUT')
    print('        3 ---------- DEBIT SPREAD')
    print('        q ---------- QUIT')
    print('\n')
    
    usr_input = input("CHOOSE OPTION TYPE: ")
    
    if usr_input != "q":
        if usr_input == "1":
            call_option()
        if usr_input == "2":
            put_option()
        if usr_input == "3":
            debit_spread()
        else:
            main()
    else:
        os.system('clear')
        quit()

        

def main():
    display()
    menu()

main()


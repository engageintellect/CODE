import os
import subprocess



def display():
    os.system('clear')
    os.system('figlet OPTIONS')

    
def call_option():
    display()
    print('=== CALL OPTION ===\n')
    current_price =     float(input("CURRENT STOCK PRICE: $"))
    strike_price =      float(input("STRIKE PRICE: $"))
    premium_price =     float(input("PREMIUM PRICE: $"))
    price_target =      float(input("STOCK TARGET PRICE: $"))
    profit_per_share =  float(price_target - strike_price - premium_price)
    potential_profit =  float(profit_per_share * 100)
    profit = "%.2f" % potential_profit
    print("\n")
    print(f'PREMIUM:            ${premium_price * 100}')
    print(f'BREAK EVEN:         ${premium_price + strike_price}')
    print(f'POTENTIAL LOSS:     ${premium_price * 100}')
    print(f'POTENTIAL GAIN:     ${profit}')
 
def put_option():
    display()
    print('=== PUT OPTION ===\n')
    current_price =     float(input("CURRENT STOCK PRICE: $"))
    strike_price =      float(input("STRIKE PRICE: $"))
    premium_price =     float(input("PREMIUM PRICE: $"))
    price_target =      float(input("STOCK TARGET PRICE: $"))
    profit_per_share =  float(strike_price - price_target - premium_price)
    potential_profit =  float(profit_per_share * 100)
    profit = "%.2f" % potential_profit
    print("\n")
    print(f'PREMIUM:            ${premium_price * 100}')
    print(f'BREAK EVEN:         ${premium_price + strike_price}')
    print(f'POTENTIAL LOSS:     ${premium_price * 100}')
    print(f'POTENTIAL GAIN:     ${profit}')



def main():
    display()
    print('[ SELECT OPTION TYPE ]\n')
    print('CALL OPTION ------ 1')
    print('PUT OPTION ------- 2')
    print('\n')

    option_type = input("> ")
    if option_type == 'q':
        os.system('clear')
        quit()
            
    if option_type == '1':
        call_option()
    elif option_type == '2':
        put_option()
    else:
        print("Please select a valid option...")
        main()







main()

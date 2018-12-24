    ####################################################
    #
    #   Algorithm
    #   Takes purchase price and amount of dollars paid
    #   Prints how many of each coins are needed to create correct amount of change
    #   Runs until stock is out of change
    #
    ###################################################

import sys

#Values of coins, Stock, & # of coins given for change
quarter = .25
dime = .10
nickel = .05
penny = .01
stock_quarters = 10
stock_dimes = 10
stock_nickels = 10
stock_pennies = 10
num_quarters = 0
num_dimes = 0
num_nickels = 0
num_pennies = 0

#Prompt user
print("\nWelcome to change-making program.")
price = input("Enter the purchase price (xx.xx) or `q' to quit: ")
if float(price) < 0:
    print("Error: purchase price must be non-negative.")
    
#Loop to find how many of each coin is given back and how many of each coin is left
while price.lower() != 'q':
    dollars_paid = int(input("Input dollars paid (int): "))
    price = float(price)
    change = dollars_paid - price
    if dollars_paid > price:
        while (change - quarter) >= 0:
            stock_quarters -= 1
            num_quarters += 1
            change -= quarter
            if stock_quarters == -1:
                sys.exit("Error: ran out of coins.")
        while (change - dime) >= 0:
            stock_dimes -= 1
            num_dimes += 1
            change -= dime
            if stock_dimes == -1:
                sys.exit("Error: ran out of coins.")
        while (change - nickel +.001) >= 0:
            stock_nickels -= 1
            num_nickels += 1
            change -= nickel
            if stock_nickels == -1:
                sys.exit("Error: ran out of coins.")
        while (change - penny + .001) >= 0:
            stock_pennies -= 1
            num_pennies += 1
            change -= penny
            if stock_pennies == -1:
                sys.exit("Error: ran out of coins.")
        print("Collect payment below:")
        if num_quarters != 0:
            print("Quarters: " + str(num_quarters))
        if num_dimes != 0:
            print("Dimes: " + str(num_dimes))
        if num_nickels != 0:
            print("Nickels: " + str(num_nickels))
        if num_pennies != 0:
            print("Pennies: " + str(num_pennies))
        print("Stock: " + str(stock_quarters) + " quarters, " + str(stock_dimes) + " dimes, " + str(stock_nickels) + " nickels, and " + str(stock_pennies) + " pennies")
    else:
        print("Error: insufficient payment.")
    num_quarters = 0
    num_dimes = 0
    num_nickels = 0
    num_pennies = 0
    price = input("Enter the purchase price (xx.xx) or `q' to quit: ")
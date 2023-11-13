# MODULES
import random

MAX_LINES = 3 # constant values are in all caps
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = { # dictionary
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items(): # gets key and value
        for _ in range(symbol_count): # _ anonymous value
            all_symbols.append(symbol)
    
    columns = [] # columns list
    for _ in range(cols):
        column = [] 
        current_symbols = all_symbols[:] # : slice operator (copy of all_symbols list)
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column) # add column to column list
        
    return columns

def deposit(): # function
    while True:
        amount = input("What would you like to deposit? $") # prompt
        if amount.isdigit(): # check that amount is a valid number
            amount = int(amount) # convert amount input from string to a number(integer)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero.")
        else:
            print("Please enter a number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit(): # check that amount is a valid number
            lines = int(lines) # convert amount input from string to a number(integer)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter valid number of lines.")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $") # prompt
        if amount.isdigit(): # check that amount is a valid number
            amount = int(amount) # convert amount input from string to a number(integer)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}.")

main()

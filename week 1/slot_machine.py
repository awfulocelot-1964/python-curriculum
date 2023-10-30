# slot machine
# imports
import random


# constants:
MAX_LINES = 3
MAX_BET = 1000

ROWS = 3
COLS = 3

# symbol count
symbol_count = {"SS": 1, "S": 2, "A": 4, "B": 8, "C": 16, "D": 32, "F": 64}

# 1/128 (0.078%) chance of jackpot


# define a function for the slot machine spin
# with parameters (rows, cols, symbols)
def slot_spin(rows, cols, symbols):
    all_symbols = []
    for symbol in symbols:
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        column.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], "|")
            else:
                print(column[row])


# decorator
def my_decorator(func):
    def wrapper():
        print(f"running {func.__name__}")
        func()
        print("complete")

    return wrapper()


# define deposit function:
# @my_decorator
def deposit():
    while True:
        deposit_amount = input("enter the amount you'd like to deposit: $")
        if deposit_amount.isdigit() and int(deposit_amount) > 0:
            deposit_amount = int(deposit_amount)
            break
        else:
            print("input must be a number above 0.")
    return deposit_amount


# define number of lines function:
# @my_decorator
def get_number_of_lines():
    while True:
        number_of_lines = input(
            f"enter how many lines you'd like to bet on (1 — {MAX_LINES} lines): "
        )
        if number_of_lines.isdigit():
            number_of_lines = int(number_of_lines)
        if 1 <= number_of_lines <= MAX_LINES:
            break
        else:
            print(f"enter a number between 1 and {MAX_LINES}.")
    return number_of_lines


# define main function:
# @my_decorator
def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        total_bet = input("what would you like to bet on each line? ")
        if total_bet.isdigit():
            total_bet = int(total_bet)
        if total_bet > balance:
            print(
                f"you've bet more than your balance (enter a number between 1 and {balance})!"
            )
        else:
            break

    div_bet = int(total_bet / lines)
    print(f"you are betting ${div_bet} on {lines} lines. total bet is {total_bet}")

    slots = slot_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)


main()

import os

# define variables outside function
fnumber = 0
snumber = 0
operator = " "


# define a function to clear the console
def clear_console():
    command = "clear"
    os.system(command)


# define function for arithmetic
def arithmetic():
    fnumber = int(input("enter your first number: "))
    fnumber = int(fnumber)

    snumber = int(input("enter your second number: "))
    snumber = int(snumber)

    operator = input("enter your arithmetic operator (a, s, m, d): ")
    operator = operator.lower()

    if operator == "a":
        print(f"the sum of {fnumber} and {snumber} is {fnumber + snumber}.")

    elif operator == "s":
        print(f"the difference of {fnumber} and {snumber} is {fnumber - snumber}.")

    elif operator == "m":
        print(f"the product of {fnumber} and {snumber} is {fnumber * snumber}.")

    elif operator == "d":
        if snumber == 0:
            print("undefined! did you divide by zero?")
        else:
            print(f"the quotient of {fnumber} and {snumber} is {fnumber / snumber}.")

    else:
        print(f"invalid operator {operator}!")

    return fnumber, snumber, operator


while True:
    clear_console()
    arithmetic()
    another_calculation = input("would you like to do another calculation (y/n)? ")
    if another_calculation != "y":
        break


# get first, second number
# get operator
# print answer

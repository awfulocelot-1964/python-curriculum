# data types

data = "day 1"

# data types:
# ————————————————
# comfortable wwith
str = "string"  # string
int = 1  # integer
float = 1.0  # float
complex = 1j  # complex
bool = True  # bool
list = ["apple", "banana", "cherry"]  # list
range = range(6)  # range

# need to study
tuple = ("apple", "banana", "cherry")  # tuple
dict = {"name": "John", "age": 36}  # dict
set = {"apple", "banana", "cherry"}  # set (no duplicates)
bytes = b"Hello"  # bytes
none = None  # none
methods = len(data)  # methods

# exercises
# REWRITE (specify data types)

x = str("string")
x = int(2)
x = float(2.0)
x = complex(2.0j)
x = bool(False)
x = list("artichoke", "broccoli", "crayons")
x = range(0, 5)

# if i want to convert x from an integer to a floating point,
# what would i type?

x = 5
x = float(x)

# if i wanted to use the len method to print the length of x,
# what would i type?

x = "Hello world"
print(len(x))

# methods
# ———————
# comfortable with

# need to study
length_of_data = len(data)  # len
#   will grab the length of the data
get_characters = data[1:3]
data.strip()  # strips whitespace
data.upper()  # uppercases characters
data.lower()  # lowercases characters
data.replace("a", "b")  # replaces characters
data.append(0)  # add data to a list

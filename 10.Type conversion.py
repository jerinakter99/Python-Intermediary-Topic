# type conversion means convert the type
# This can be done either implicitly (automatic) or explicitly (manual).


# 1. explicit : Done using built-in functions like int(), float(), str(),

# int(): Converts a value to an integer
x = "10"
y = int(x)
print(y)


# float(): Converts a value to a float
x = "10.5"
y = float(x)
print(y)

# str(): Converts a value to a string.
x = 10
y = str(x)
print(y)

# tuple(): Converts a value to a tuple.
x = [1, 2, 3]
y = tuple(x)
print(y)

# set(): Converts a value to a set
x = [1, 2, 3, 3]
y = set(x)
print(y)

# list(): Converts a value to a list.
x = (1, 2, 3)
y = list(x)
print(y)

# dict(): Converts a value to a dictionary
x = [("a", 1), ("b", 2)]
y = dict(x)
print(y)

# chr(): Converts an integer to a character
x = 97
y = chr(x)
print(y)


# 2. Implicit : Done automatically by Python when performing operations involving different types.
# from int to float
x = 10
y = 10.5
z = x + y
print(z)

# int to complex:
x = 10
y = 3 + 4j
z = x + y
print(z)

# //
age = input("Enter your age: ")
age = int(age)  # Convert string input to integer
print(f"Next year, you will be {age + 1} years old.")

#Packing refers to collecting multiple values into a single iterable (like a list or tuple).
# often functions that take a variable number of arguments using *args for positional arguments
# and **kwargs for keyword arguments.
# We use two operators * (for tuples) and ** (for dictionaries).

def packer(*args):
    print(args)

packer(1, 2, 3)


def mySum(*args):
    return sum(args)
print(mySum(1, 2, 3, 4, 5))
print(mySum(10, 20))

#Unpacking
# Unpacking refers to the process of splitting a collection into individual elements.
# This can be done using the * operator for sequences and ** for dictionaries
def unpacker(a, b, c):
    print(a, b, c)

args = (1, 2, 3)
unpacker(*args)

kwargs = {'a': 4, 'b': 5, 'c': 6}
unpacker(**kwargs)

def fun(a, b, c, d):
	print(a, b, c, d)

# Driver Code
my_list = [1, 2, 3, 4]

# Unpacking list into four arguments
fun(*my_list)

# ** is used for dictionaries
# A sample program to demonstrate unpacking of
# dictionary items using **
def fun(a, b, c):
	print(a, b, c)

# A call with unpacking of dictionary

d = {'a':2, 'b':4, 'c':10}
fun(**d)

#Function Calling
#Once we defined a function or finalized structure, we can call that function by using its name. We can also call that function from another function or program by importing it.
# To call a function, use the name of the function with the parenthesis, and if the function accepts parameters, then pass those parameters in the parenthesis.
# define a function and call it using its name followed by parentheses containing any arguments.

def greet(name):
    return f"Hello, {name}!"

# Function call
print(greet("Alice"))

# function
def even_odd(n):
    # check numne ris even or odd
    if n % 2 == 0:
        print('Even number')
    else:
        print('Odd Number')

# calling function by its name
even_odd(19)


#Yield
#The yield keyword is used in Python to turn a function into a generator. Instead of returning a single value,
# a generator yields a sequence of values over time, pausing after each one until the next value is requested

def generate_numbers():
    for i in range(4):
        yield i

# Using the generator
for number in generate_numbers():
    print(number)


#Recursive Function

# A recursive function is a function that calls itself, again and again.
# Recursion is useful for tasks that can be defined in terms of similar subtasks.
# Consider, calculating the factorial of a number is a repetitive activity,
# in that case, we can call a function again and again, which calculates factorial
# They are useful for tasks that can be broken down into similar subtasks
# traversing data structures (like trees and graphs),
# solving mathematical problems (like calculating factorials and Fibonacci sequences),
# Base Case: The condition that stops the recursion.
# Recursive Case: The part of the function where it calls itself, working towards the base case.

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Function call

print(factorial(5))



def numbers(end,start=0):
    if start==end:
        return 1000
    start+=1
    return numbers(end,start=start)
print(numbers(3))

#Fibonacci sequence is a series of numbers in which each number (after the first two) is the sum of the two preceding ones
#0,1,1,2,3,5,8,13,21,34,…
# The sequence starts with two initial values: 0 and 1
# Each subsequent number is the sum of the previous two numbers
def fib(n):
    a=0
    b=1

    print(a)
    print(b)
    for i in range (2,n):
        c=a+b
        a=b
        b=c
        print(c)


fib(10)

#//recursive
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Test the recursive function
n = 10
for i in range(n):
    print(fibonacci_recursive(i), end=" ")

#fibonacci

def fibo (n):
  if n<=0:
      return 0
  elif n==1:
      return 1
  else:
      return fibo(n-1)+fibo(n-2)      # recursive function

n=5  #(0-5)
for i in range (n):
  print(fibo(i), end=" ")         #fibo(0),fibo(1),fibo(2).....fibo(4)














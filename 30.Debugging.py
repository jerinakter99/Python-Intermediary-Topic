# if we don't get our expected ouutput then we go for degug the program,then we can see
#  how the program execute step by step
# debugging : it is step by step process , where we can find out the problem/error and we can go for solution
# where is wrong to find out we need to put debugger

# 2 ways we can do debugging/Debugger
# 1. pdb (when u r in hurry)
# 2. run with debug(understandable)

#   Debugging is the process of identifying, analyzing, and resolving bugs or defects in software.
#   Bugs can be syntax errors, logical errors, runtime errors, or any issue that causes the program
#   to behave unexpectedly or incorrectly. The goal of debugging is to understand why the software is not
#   functioning as intended and to fix the underlying issues to ensure the software works correctly


# ex1

import pdb

f = "jerin "
pdb.set_trace()
l = "akter"
name = f + l
print(name)

# ex2
def addition(a, b):
    answer = a * b
    return answer

pdb.set_trace()
x = input("Enter first number : ")
y = input("Enter second number : ")
sum = addition(x, y)
print(sum)
#
a=5
b=0
try:
 c=a/b
except ZeroDivisionError:
    print("dont divide by zero")


# pdb stands for Python Debugger, which is a built-in module in Python that allows you to interactively debug
#  your programs. It provides a way to set breakpoints, step through your code, inspect variables,
#  and understand the flow of your program in a controlled manner.
#
# Key Features of pdb
# Breakpoints: You can pause the execution of your program at specific points to inspect the state of your variables and the flow of your program.
# Stepping Through Code: You can execute your program line by line to see exactly what it does at each step.
# Inspecting Variables: You can check the values of variables at any point during execution.
# Interactive Commands: pdb provides a command-line interface to control the execution and inspect your program.
# How to Use pdb
# Setting Up a Breakpoint
# You can set a breakpoint using pdb.set_trace() in your code. When the program execution reaches this point, it will pause, and you can start debugging.
#
# Example:
#
# python
# Copy code
# import pdb
#
# def add(a, b):
#     pdb.set_trace()  # Pause execution here
#     return a + b
#
# result = add(5, 10)
# print(f'Result: {result}')
# Running the Code
# When you run the above script, the execution will pause at the pdb.set_trace() line, and you will enter the pdb interactive mode.
#
# sh
# Copy code
# $ python script.py
# > script.py(5)add()
# -> return a + b
# (Pdb)
# Basic pdb Commands
# l (list): Show the current location in the code.
# n (next): Execute the next line of code.
# s (step): Step into the function call.
# c (continue): Continue execution until the next breakpoint.
# q (quit): Exit the debugger and stop the program.
# p (print): Print the value of a variable.
# Example Usage:
#
# sh
# Copy code
# (Pdb) l  # List the code around the current line
#   1     import pdb
#   2
#   3     def add(a, b):
#   4         pdb.set_trace()  # Pause execution here
#   5  ->     return a + b
#   6
#   7     result = add(5, 10)
#   8     print(f'Result: {result}')
# (Pdb) n  # Move to the next line
# > script.py(7)<module>()
# -> result = add(5, 10)
# (Pdb) p a  # Print the value of 'a'
# 5
# (Pdb) p b  # Print the value of 'b'
# 10
# (Pdb) c  # Continue execution
# Result: 15

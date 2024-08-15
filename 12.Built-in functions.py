# map,filter, reduce
# All three of these are convenience functions that can be replaced with List Comprehensions or loops
# but offer a more elegant and concise solution to some problems.
# They allow you to apply a function to a sequence of elements (like a list) and return another sequence

# map()
# map() function is used to apply some functionality for every element present in the given sequence
#      and generate a new series with a required modification
# The map() function applies a given function to all items in an input list (or any other iterable)
# and returns a map object (which can be converted into a list, set, etc.).

# Syntax: map(function, iterable, ...)
#function: A function that will be applied to each element of the iterable.
#iterable: An iterable object like a list, tuple, etc., to be mapped.

#EX.given a string in array map each value to int and return a int list

sarr=["1","2","3","4","5",]
int_arr=map(int,sarr)
print(list(int_arr))

#Or

int_arr = [1,2,3,4]
str_arr = map(str, int_arr)
print(list(str_arr))

# Convert a list of strings to integers
strings = ["1", "2", "3", "4"]
integers = list(map(int, strings))
print(integers)

# Square each number in a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)

# filter()
# function is used to return the filtered value
#The filter() function creates a new iterator that filters elements from a previously created one (like a list, tuple, or dictionary).
#The filter() function checks whether or not the given condition is present in the sequence and then prints the result
#function − The function to be used in the code,
# Function argument is responsible for performing condition checking
# Sequence argument can be anything like list, tuple, string

#iterable − This is the value that is iterated in the code.An iterable object like a list, tuple, etc., to be filtered.

# Filter out even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# Filter out non-positive numbers
numbers = [-1, 0, 1, 2, -2]
positive_numbers = list(filter(lambda x: x > 0, numbers))
print(positive_numbers)

# creating a function that returns the eligibility ages for voting from the list

def votingAge(givenNumumber):

   if givenNumumber>=18:
      return givenNumumber
inputList = [3, 20, 18, 6, 14, 25, 19]
# Getting only values of above list which are greater than or equal to 18
result_filterObj = filter(votingAge, inputList)
# printing the filter object
print(result_filterObj)
# converting into a list
print("Eligibile ages for voting :", list(result_filterObj))


#reduce()
# reduce() function is used to minimize sequence elements into a single value by applying the specified condition.
#the reduce() function iterates through each item in a list or other iterable data type, returning a single value.
#reduce(function, iterable)

# importing reduce() function from functools module
from functools import reduce
# function that returns the sum of all list items
def addNumbers(x, y):
   return x+y
# input list
inputList = [12, 4, 10, 15, 6, 5]
# Print the sum of the list items using reduce() function
print("The sum of all list items:")
print(reduce(addNumbers, inputList))

# it will take two elements of the list and sum them to make one element,
# then take another list element and sum it again to make one element,
# and so on until it sums all of the list's elements and returns a single value.
from functools import reduce

# Calculate the sum of a list of numbers
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)  # Output: 15

# Calculate the product of a list of numbers
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120

from functools import reduce

# Given a list of numbers, find the sum of the squares of the even numbers
numbers = [1, 2, 3, 4, 5, 6]

# Step 1: Filter out the even numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)

# Step 2: Square the filtered numbers
squared_even_numbers = map(lambda x: x ** 2, even_numbers)

# Step 3: Sum the squared numbers
sum_of_squares = reduce(lambda x, y: x + y, squared_even_numbers)

print(sum_of_squares)

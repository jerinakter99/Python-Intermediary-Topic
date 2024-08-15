#Iterable is something(collection anything) that allows some kind of iteration on its elements.
# An interable is an object like a list, string, or tuple that contains other objects that it can return one at a time
# doing loop
# an iterable is any object that can be looped over (iterated over) using a loop construct such as a for loop.
# # An iterable must implement the special method __iter__() that returns an iterator.
# Common Iterables
# Lists: [1, 2, 3, 4]
# Tuples: (1, 2, 3, 4)
# Strings: "hello"
# Dictionaries: {'a': 1, 'b': 2}
# Sets: {1, 2, 3, 4}
# Files: File objects in Python are also iterable


class MyIterable:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


my_iterable = MyIterable([1, 2, 3, 4])

for item in my_iterable:
    print(item)


# a non-iterable is an object that does not support iteration.
# Non-iterables in Python are objects that do not support iteration
# because they do not implement the necessary methods (__iter__() or __getitem__()).
# Common non-iterables include integers, floats, booleans,
# and instances of custom classes that do not define these methods.

# # Common examples of non-iterable objects include:
# Integers: e.g., 42
# Floats: e.g., 3.14
# Booleans: e.g., True, False
# NoneType: e.g.,

number = 42

try:
    for digit in range (number):
        print(digit)
except TypeError as e:
    print(f"Error: {e}")
 # but can print int value by range

try:
    for digit in range (number):
        print(digit)
except TypeError as e:
    print(f"Error: {e}")



#How to Fix Int Object is Not Iterable
# count = 14
#
# for i in count:
#     print(i)


#fix

count=15
for i in range(count):
    print(i)

n=10
for i in range(n):
    print(i)

age=6
print("Enter the age no:")
for num in range(age):
    print(num)






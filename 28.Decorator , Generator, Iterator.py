# decorator is a function jeta onno ekta function k wrape kore extend kore modify korte pare
# behavior gulo change kore dite pare

# In Python, decorators are a powerful and flexible way to modify the behavior of a function or a method.
# They allow you to wrap another function to extend its behavior without permanently modifying it.
# Decorators are often used for logging, access control, instrumentation, caching, and more.
# offering a clean, readable, and efficient way to extend the behavior of functions and methods.
# A decorator is a function that takes another function and extends its behavior. The basic syntax for a decorator is:
def my_decorator(func):
     def wrapper():
            print("Something is happening before the function is called.")
            func()
            print("Something is happening after the function is called.")

     return wrapper


@my_decorator
def say_hello():
    print("Hello!")
say_hello()

# How Decorators Work
# Define the Decorator Function: This function will wrap another function.
# Define the Wrapper Function: Inside the decorator, define a wrapper function that will call the original function and add additional behavior before or after it.
# Return the Wrapper Function: The decorator function returns the wrapper function.
# Use the Decorator: Apply the decorator to a function using the @decorator_name syntax.


















class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def __display_balance(self):
        print("Balance:", self.__balance)


b = BankAccount(1234567890, 5000)
b.__display_balance() 
# data and function binding each other , ensure data hiding securities

# Encapsulation is the concept of wrapping data (variables) and methods (functions) together as a single unit.
# It restricts direct access to some of an object's components, which can prevent the accidental modification of data.
# It provides controlled access to the data
# Encapsulation: Focuses on hiding the internal state of an object and protecting it from unwanted modification.
# Implementation: Achieved using access modifiers to restrict access to the internal state of the object.
# Focus:     Deals with the implementation level of the system, focusing on how an object’s state is protected.
# Visibility :  Explicitly restricts access to data and provides controlled access through methods.

#  protect and organize data and functions in a logical way.
#  Think of it as a way to keep the important parts of a program private
#  and only allow certain parts to be accessed or modified in a controlled manner.

# How it Works:
# Uses access modifiers like private, protected, and public to restrict access.
# Provides getter and setter methods to access and update the value of private variables.
# to define a private member prefix the member name with double underscore “__”.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

# Using the encapsulated class
account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())

# Ex2
class Employee:
    def __init__(self, name, salary):
        self.__name = name  # Private attribute
        self.__salary = salary  # Private attribute

    # Public method to get the name
    def get_name(self):
        return self.__name

    # Public method to set the name
    def set_name(self, name):
        self.__name = name

    # Public method to get the salary
    def get_salary(self):
        return self.__salary

    # Public method to set the salary
    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid salary amount!")


emp = Employee("John Doe", 50000)

# Accessing and modifying the attributes using public methods
print(emp.get_name())
emp.set_name("Jane Doe")
print(emp.get_name())

print(emp.get_salary())
emp.set_salary(55000)
print(emp.get_salary())

# Trying to set an invalid salary
emp.set_salary(-100)

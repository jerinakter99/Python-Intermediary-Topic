# Access modifiers in programming are keywords or symbols used to define the accessibility of
# variables,methods, or classes. They control where and how these members can be accessed within a program
# Public: Accessible from anywhere; no special prefix.
# Protected: Intended for internal use within the class and subclasses; single underscore _ prefix.
# Private: Intended for internal use within the class only; double underscore __ prefix.

class Access:
    def __init__(self,a,b,c):
        self.public=a          # public attribute _can access anywhere of the programe
        self._protected=b     # protected attribute _ it shouulld not be accessed directly outside the class and the subclasses
        self.__private=c     #  dificullt to access outside the class

v=Access('A','B','C')
print(v.public)
v._protected='P' # i can access a protected variable
print(v._protected)
# print(v.__private)      cant access private variable outside of the class
print(v._Access__private)     # _className__attribute # by name mangling we can access
# name mangling : its a technique to acces private attributes directly ouutside the class





# 1. Public Members

# Public members are accessible from outside the class. By default, all members of a class in Python are public.

class MyClass:
    def __init__(self, name):
        self.name = name  # Public attribute // attributes means what class has

    def display_name(self):
        print(f"Name: {self.name}")  # Public method // method means what class does

obj = MyClass("John")
print(obj.name)  # Accessing public attribute
obj.display_name()  # Accessing public method


# The members of a class that are declared protected are only accessible to a class derived from it.
# Protected members can be accessed within the class and its subclasses.
# They are not intended to be accessed directly from outside the class, though it is possible.
# Protected members are indicated by a single underscore (_) prefix.
# Accessed within the class and its subclasses

class Trader :
    def __init__(self):
        self.Indicators= "Supertrend"
        self._SetUp="indicator setup"
        self.__Profit="percentage of profit"

class Mock_trader(Trader):
    pass
mt=Mock_trader()
print(mt.Indicators)
print(mt._SetUp)
print(mt.__Profit)
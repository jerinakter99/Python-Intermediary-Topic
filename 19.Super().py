#access the property ,easy to access property from parent class
#Allows us to avoid using the base class name explicitly
#Working with Multiple Inheritance
#super() = fuunction used in a child class to call methods from a parent class (superclass)
#          allows to extend the functionality of the inherited methods.
#super() with Single Inheritance
# class A():
#     def __init__(self, AName):
#         self.Aname = AName
#         print(AName, 'is a student.')
#
#
# class B(A):
#     def __init__(self,AName):
#         self.Aname = AName
#
#         print('Jhon has a laptop')
#     super().__init__("a")  # eita constructor er moto kaj kore ,
#            # jokhon super keyword use korbo tokhon automatic sob value gulo base cls theke inherit korbe
#
# d1 = B()


#super() with Multiple Inheritance :

# In multiple inheritence if I use super then check it is accessible by derived class or not ,
# super use kore amra sequncially method gulo call korte pari
# super mro maintain kore , it maintain the order in which methods are called and execute.
# super() is used to represent, calls to parent classes following the method resolution order (MRO).
# This ensures that methods are called in the correct order according to the inheritance hierarchy.
# ex1
class B:
    def __init__(self):
        print("A is inherit")

class A:
    def __init__(self):
        super().__init__()
        print("B is inherit")

class D(A,B):
    def __init__(self):
        super().__init__()
        print("D is inherit")

d=D()

# 2
class B:
    def __init__(self):
        print("B's init ")

    def jerin(self):
        print("jony")

class A:
    def __init__(self):
        super().__init__()
        super().jerin()
        print("A's init")

    def maya(self):
        print("Jeny")

class D(A,B):
    def __init__(self):
        super().__init__()
        super().maya()
        print("D's init")

d=D()
print(D.mro())

# d = D() triggers the __init__ method of D.
# super().__init__() in D.__init__ calls A.__init__.
# super().__init__() in A.__init__ calls B.__init__, which prints "B's init ".
# super().jerin() in A.__init__ calls B.jerin(), which prints "jony".
# print("A's init") in A.__init__ prints "A's init".
# super().maya() in D.__init__ calls A.maya(), which prints "Jeny".
# print("D's init") in D.__init__ prints "D's init"

# What super() Does
# super().__init__() in D.__init__: This call moves up the MRO and invokes A.__init__.
# super().__init__() in A.__init__: This call further moves up the MRO and invokes B.__init__.
# super().jerin() in A.__init__: This call moves up the MRO from A and invokes B.jerin.
# super().maya() in D.__init__: This call moves up the MRO from D and invokes A.maya.
# super() dynamically looks up the next class in the MRO and calls the specified method on it.
# super().__init__() calls the __init__ method of the next class in the MRO.
# super().jerin() calls the jerin method of the next class in the MRO.
# super().maya() calls the maya method of the next class in the MRO.
# The MRO ensures that methods are called in the correct order, respecting the inheritance hierarchy.


# Without super:

# explicitlly : “clearly”, “plainly”, “openly”, or “directly”

# If you don't use super() in the code, you will need to explicitly call the __init__ methods and other methods
# from the parent classes. This can lead to more complex and error-prone code,
# especially in the case of multiple inheritance where method resolution order (MRO) is crucial.


class B:
    def __init__(self):
        print("B's init ")

    def jerin(self):
        print("jony")

class A:
    def __init__(self):
        B.__init__(self)
        B.jerin(self)
        print("A's init")

    def maya(self):
        print("Jeny")

class D(A, B):
    def __init__(self):
        A.__init__(self)
        A.maya(self)
        print("D's init")

d = D()
# Without super(), you need to manually call the __init__ methods and other methods of the parent classes.
# B.__init__(self) and B.jerin(self) are called explicitly in A.__init__.
# A.__init__(self) and A.maya(self) are called explicitly in D.__init__.

# Using super() in multiple inheritance scenarios ensures that methods are called in the correct order according to the MRO,
# making the code more maintainable and less error-prone.
# Explicitly calling methods without super() can work but is generally not  recommended due to increased complexity and potential for errors.
#
#  Using super():Handles the diamond problem (where multiple inheritance paths converge on a common ancestor) gracefully by following the MRO.
#  Automatically handles MRO, more maintainable, flexible, cleaner code, handles diamond problem well.
#
# # Without super(): Can lead to redundant calls and harder-to-manage code in diamond inheritance scenarios.


#
# Using super() with multiple parameters in multiple inheritance ensures that arguments are passed correctly
# up the chain of constructors according to the MRO.
# Each class in the hierarchy only needs to call super() with the appropriate subset of arguments,
# allowing for clean and maintainable code
#
# When working with super() in Python, especially in the context of multiple inheritance and multiple parameters,
# it’s important to understand how to correctly pass arguments up the chain of constructors
# ( or other methods) in the inheritance hierarchy.
# super() helps to ensure that the arguments are passed to the correct methods
# according to the method resolution order (MRO).
class B:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(f"B's init with x={x}, y={y}")

class A:
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
        print(f"A's init with z={z}")

class D(A, B):
    def __init__(self, x, y, z, w):
        super().__init__(x, y, z)
        self.w = w
        print(f"D's init with w={w}")

d = D(1, 2, 3, 4)

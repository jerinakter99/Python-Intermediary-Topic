# The diamond problem occurs in multiple inheritance when a class inherits from two classes
#       that have a common base class. This can create ambiguity in method resolution,
#       as it's unclear which path to follow to access attributes and methods from the common base class.
#       Python resolves this issue using the C3 linearization algorithm,
#       which determines a method resolution order (MRO).

#The diamond problem is a well-known issue in multiple inheritance in object-oriented programming.
#It arises when a class inherits from two classes that both inherit from a common base class# how MRO works
#  it requires careful design to avoid complications such as the diamond problem.
#  Python's method resolution order (MRO) and the super() function
#  help manage method calls and attribute lookups in classes that use multiple inheritance.
# Diamond Problem
# The diamond problem occurs when a derived class inherits from two classes that have a common base class.
# Python handles this using the C3 linearization algorithm for method resolution order (MRO).

# Scinario of diamond problem

class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print(D.mro())


# //
class A:
    def say_hello(self):
        return "Hello from A"
class B(A):
    def say_hello(self):
        return "Hello from B"

class C(A):
    def say_hello(self):
        return "Hello from C"
class D(B, C):
    pass
d = D()
print(d.say_hello())  # Output: Hello from B (due to MRO)
print(D.mro())

# here ,class D inherits from both B and C, which both inherit from A.
# The method resolution order is determined by the C3 linearization,
# and Python chooses the method from B first because B is listed before C in the inheritance list.

class A:
    def rk(self):
        print(" In class A")


class B(A):
    def rk(self):
        print(" In class B")

r = B()
r.rk()

class A:
    def rk(self):
        print(" In class A")

class B(A):
    def rk(self):
        print(" In class B")

class C(A):
    def rk(self):
        print("In class C")

# classes ordering
class D(B, C):
    pass

r = D()
r.rk()
class Animal:
    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.species

class Walkable(Animal):
    def walk(self):
        return f"{self.get_species()} is walking"

class Swimmable(Animal):
    def swim(self):
        return f"{self.get_species()} is swimming"
class Duck(Walkable, Swimmable):
    def __init__(self, species):
        super().__init__(species)
duck = Duck("Duck")
print(duck.walk())   # Output: Duck is walking
print(duck.swim())   # Output: Duck is swimming
print(Duck.mro())

# Duck inherits from both Walkable and Swimmable, which both inherit from Animal.
# The MRO ensures that Animal is initialized only once, and methods from Walkable and Swimmable are correctly resolved.

# Method Overriding with Diamond Problem
class A:
    def say_hello(self):
        return "Hello from A"
class B(A):
    def say_hello(self):
        return "Hello from B"

class C(A):
    def say_hello(self):
        return "Hello from C"
class D(B, C):
    def say_hello(self):
        return "Hello from D, " + super().say_hello()
d = D()
print(d.say_hello())  # Output: Hello from D, Hello from B
print(D.mro())
# class D overrides the say_hello method and uses super().say_hello() to call the next method in the MRO.
# The output reflects the order of method resolution.


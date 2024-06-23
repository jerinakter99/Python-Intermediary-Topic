#Object-oriented programming (OOP)

class No: #create class no
    a=5
obj=No() #create object obj
print(obj.a)

#__init__ function
class Me:
    def __init__(self,name ,age):
        self.name=name
        self.age=age

obje=Me("oli" ,23)
print(obje.name)
print(obje.age)

#Inheritance in Python allows one class (subclass or derived class)
# to inherit attributes and methods from another class (superclass or base class).
class A:
    def feature1(self):
        print("feature 1 working")
    def feature2(self):
        print("feature 2 working")


class B(A):
    def feature3(self):
        print("feature 3 working")
    def feature4(self):
        print("feature 4 working")

class C(B):
    def feature5(self):
        print("feature 5 working")

a1=A()

a1.feature1()
a1.feature2()

b1=B()

b1.feature3()
b1.feature4()
c1=C()
c1.feature5()

#Single inheritence

class bird: # Base class
    def __init__(self,name):
        self.name=name

    def sound(self):
        return "make sound"
class Parrot(bird):  # Derived class inheriting from bird
    def sound(self):
        return "make sound hhhh"
parrot=Parrot("parro")
print(parrot.name)
print(parrot.sound())

# Multiple inheritance
# a subclass can inherit from multiple base classes

# Base class 1
class B1:
    def __init__(self, name):
        self.name = name

    def B1method(self):
        return "animalname"

# Base class 2
class B2:
    def __init__(self, type):
        self.type = type

    def B2method(self):
        return "animaltype"

# Derived class_De inheriting from B1,B2
class De(B1, B2):
    def __init__(self, name):
        B1.__init__(self, name)
        B2.__init__(self, "animal")


    def B1method(self):
        return "dog"

obj = De("cat")

print(obj.B1method())
print(obj.B2method())
print(obj.name)
print(obj.type)




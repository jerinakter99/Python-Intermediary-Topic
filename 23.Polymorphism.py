# The word polymorphism means having many forms.
# Polymorphism is like one interface, many implementations.
# polymorphism means the same function name (but different signatures) being used for different types
# methods/functions/operators with the same name that can be executed on many objects or classes.
# 1.fuunction overloading
# 2.function overriding
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

def print_area(shape):
    print(shape.area())



# Create instances of Circle and Rectangle
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Call the same method area() on different objects
print_area(circle)      # Output: 78.5
print_area(rectangle)   # Output: 24

#  you have a shape object. You can have different types of shapes like circle, rectangle, and triangle.
#  Each shape can have a method called area to calculate its area,
#  but the way the area is calculated is different for each shape.

# Types of Polymorphism
# Compile-Time Polymorphism (Method Overloading)
# Run-Time Polymorphism (Method Overriding):
#
# Method Overriding
# Method overriding occurs when a subclass provides a specific implementation for a method that is already defined in its superclass.
# Conditions of Method Overriding:
#
# There should be inheritance. Within a class, function overriding is not possible, therefore a child class is derived from a parent class.
# A function of the child class should have the same number of parameters as that of the parent class.

class Animal:
    def make_sound(self):
        return "Some generic sound"


class Dog(Animal):
    def make_sound(self):
        return "Bark"


class Cat(Animal):
    def make_sound(self):
        return "Meow"


def animal_sound(animal):
    print(animal.make_sound())


# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

# Call the same method make_sound() on different objects
animal_sound(dog)  # Output: Bark
animal_sound(cat)  # Output: Meow
# In this example, the make_sound method is overridden in the Dog and Cat classes,
# providing specific implementations for each type of animal.

class Vehicle:
    def start_engine(self):
        return "Starting the vehicle's engine"

class Car(Vehicle):
    def start_engine(self):
        return "Starting the car's engine"

def test_engine(vehicle):
    print(vehicle.start_engine())

# Create instances of Vehicle and Car
vehicle = Vehicle()
car = Car()

# Call the same method start_engine() on different objects
test_engine(vehicle)
test_engine(car)

# In this example, the start_engine method is overridden in the Car class.
# When test_engine is called with a Car object, it uses the overridden method in the Car class.


# 2.
# Method overloading is a concept where multiple methods with the same name can exist in a class, but with different parameters.
# Python does not support traditional method overloading ,you can achieve similar functionality
# using default arguments, variable-length arguments, and type checking

class MathOperations:
    def multiply(self, a, b, c=1):
        return a * b * c

math_ops = MathOperations()

# Call the multiply method with two arguments
print(math_ops.multiply(2, 3))

# Call the multiply method with three arguments
print(math_ops.multiply(2, 3, 4))

print()



# Class Polymorphism:
# We can use the concept of polymorphism while creating class methods as Python allows different classes to have methods with the same name.
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()



# Polymorphism and Inheritance:
# the child classes in Python also inherit methods and attributes from the parent class.
# We can redefine certain methods and attributes specifically to fit the child class, which is known as Method Overriding.
# Polymorphism allows us to access these overridden methods and attributes that have the same name as the parent class.
# Method Overriding:
from math import pi

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "I am a two-dimensional shape."

    def __str__(self):
        return self.name


class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length**2

    def fact(self):
        return "Squares have each angle equal to 90 degrees."


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi*self.radius**2


a = Square(4)
b = Circle(7)
print(b)
print(b.fact())
print(a.fact())
print(b.area())

# Method Overriding and Polymorphism with Inheritance is:
class Vehicle:

    def desc(self):
        print("So many categories of vehicle")

    def wheels(self):
        print("Differs according to the vehicle category")


class car(Vehicle):

    def wheels(self):
        print(4)


class bus(Vehicle):

    def wheel(self):
        print(8)


obj_vehicle = Vehicle()

obj_car = car()

obj_bus = bus()

obj_vehicle.desc()

obj_vehicle.wheels()

obj_car.desc()

obj_car.wheels()

obj_bus.desc()

obj_bus.wheels()



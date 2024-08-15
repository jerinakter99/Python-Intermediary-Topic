#*** Magic/Dunder/Special method
# magic method work with object.
#based on action magic method called implicitly/atomatically
# __str__ method  provide meaningful string representations of objects.
#some commonly used magic methods:

# 1. Initialization and Representation
#__init__(self, ...): Object constructor, called when a new object is created.
#__repr__(self): Returns an "official" string representation of the object, often used for debugging.
#__str__(self): Returns a "nice" string representation of the object, used by the print function
class Me:
    def __init__(self, name, age, bio):
        self.name = name
        self.age = age
        self.bio = bio
    def __str__(self):                         #define the __str__ method in a class,
     return f"Me {self.name},{self.age} years old ,{self.bio}"

me= Me("Jeny",23,"I am a Trader")
print(me)
#or
#print(str(Me))

class value :
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"value(x={self.x}, y={self.y})"


val = value(2, 3)
print(repr(val))

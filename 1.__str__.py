#*** Magic/Dunder/Special method
# magic method work with object
#based on action magic method called implicitly/atomatically
# __str__ method  provide meaningful string representations of objects.
class me:
    def __init__(self, name, age, bio):
        self.name = name
        self.age = age
        self.bio = bio
    def __str__(self):                         #define the __str__ method in a class,
     return f"Me {self.name},{self.age} years old ,{self.bio}"

Me=me("Jerin Akter",24,"I am a Trader")
print(Me)
#or
print(str(Me))
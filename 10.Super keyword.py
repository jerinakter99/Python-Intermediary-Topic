# Allows us to avoid using the base class name explicitly
#Working with Multiple Inheritance
#super() = fuunction used in a child class to call methods from a parent class (superclass)
#          allows to extend the functionality of the inherited methods


#super() with Single Inheritance
class A():
    def __init__(self, AName):
        print(AName, 'is a student.')


class B(A):
    def __init__(self):
        print('Jhon has a laptop')
        super().__init__('jhon')

d1 = B()

#super() with Multiple Inheritance



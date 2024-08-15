# Transaction needed abstraction ,its hide sensetive data
# Abstraction: Focuses on hiding the complex implementation details
#              and showing only the essential features of an object.
#purpose of an abstract class is to provide a common interface for its subclasses
#Abstract classes allow you to define a common interface for a group of related classes
#abstract classes in Python provide a structured way to define and enforce a common interface for a group of related classes
#atm card kinto sob data show kore na ,sensetive data k hide kore ,jeta drkr seta show kore ,

from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self): # eita sensitive data hide kore
        # Must be implemented by any non-abstract subclass
      pass
class Laptop(Computer):
    def process(self):
        print("its running")
class programmer():
    def work(self,com):
        print("solving bugs")
        com.process()

com1=Laptop()     #cannot create object of abstruct class directly it must be subclass
prog1=programmer()
prog1.work(com1)

#2
class abstract(ABC):
    @abstractmethod
    def method1(self):
        print("abstract method")
        return

    def method2(self):
        print("concrete method")


class concrete(abstract):  #Concrete Method: inherited by subclasses.
    def method1(self):
        super().method1() #using super keyword
        return


obj = concrete()
obj.method1()
obj.method2()

class Bike:
 pass
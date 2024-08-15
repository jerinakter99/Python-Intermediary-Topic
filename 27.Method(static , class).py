# instance method is work with instance variable ,
# class method work with class variable ,
# static mathod works with nothing _if we want to extra with calss nothing to do with class varible or instance varible go with static
# if want to work with instance use self keyword, if want to class variablle then use cls
class Student:
    school="IUBAT"

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):      # its instance method cz we are passing self which is belongs to particular obj.
        return(self.m1+self.m2+self.m3)/3
    @classmethod
    def getSchool(cls):
        return cls.school

                            # just inform others it is static
    @staticmethod           # can put this method anywhere of the program
    def info():
       print("this is Student Calss ")

s1 = Student(10,20,30)
s2= Student(40,45,50)

print(s1.avg())  #avg is instance method which work with object
print(Student.getSchool())
Student.info()

#class method is going to affect the actual class
#instance method is going to affect the instance meaning that we can refer self and the variables inside the instance
#static method might or might not be releted to class it can be outside or inside and it doesnt have anything to rely on from the class itself

from datetime import date
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old."

    @classmethod
    def age_from_years(cls,name,birth_year): # cls is the naming convention i can give anything whatever we want
      current_year=date.today().year
      age=current_year-birth_year
      return cls(name,age)

jerin = Person.age_from_years('jerin',1999)
print(jerin.description())

#

class Calculator:
    def __init__(self,version):
        self.version=version

    def description(self):
        print(f'currently running calculator on version : {self.version}')

    # def add_numbers(self,numbers):
    #     return sum (numbers)

calc1= Calculator(10)
calc2 = Calculator(200)
calc1.description()
# static method is just a method that can be anywhere that doesnot rely on the class

class Calculator:
    def __init__(self,version:int):
        self.version=version

    def description(self):
        print(f'currently running calculator on version : {self.version}')
    # just inform others it is static
    @staticmethod
    def add_numbers(*numbers:float()):
        return sum(numbers)

calc1= Calculator(10)
calc2 = Calculator(20)
calc1.description()
calc2.description()
print(Calculator.add_numbers(10,30.3,30))






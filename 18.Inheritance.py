# Most useful in OOP principle,and it is most beneficial because , no need to write
# duplicate code then time will be save ,so its cost efficient
# why financial benefit because time save and time is money
# Establish a relationship between classes,

#Inheritance in Python allows one class (subclass or derived class)
# to inherit attributes and methods from another class (superclass or base class).
# that allows a class to inherit properties and behaviors (methods) from another class.
# This enables the creation of a hierarchical relationship between classes, promoting code reuse and reducing redundancy.

# Base Class (Parent Class): The class whose properties and methods are inherited.
# Derived Class (Child Class): The class that inherits from the base class.
# super() Function: Used to call methods of the base class from the derived class.
# Method Overriding: The derived class can provide a specific implementation of a method that is already defined in its base class.

# Types of Inheritance
# Single Inheritance: A derived class inherits from a single base class.
# Multiple Inheritance: one child class can inherit from multiple parent classes.***
# Multilevel Inheritance: A derived class inherits from a class which is also derived from another class.
# Hierarchical Inheritance: Multiple derived classes inherit from a single base class.
# Hybrid Inheritance: A combination of two or more types of inheritance

# Single Inheritance
# Single inheritance involves one derived class inheriting from one base class

# Base cls
class Vehicle:
    def Vehicle_info(self):
     print('Inside Vehicle class')

# Child cls
class Car(Vehicle):
    def car_info(self):
      print('Inside Car class')

# Create object of Car
car = Car()

# access Vehicle's info using car object
car.Vehicle_info()
car.car_info()

# ex1:

class Tree:
    def __init__(self,color,length):
        self.tree_color=color
        self.tree_length=length
    def leaf(self):
        return f"leaf color {self.tree_color} and  length {self.tree_length }"
class Rose(Tree):
    def flower(self):
        return "Rose is a flower"

rose=Rose("Red",35)
print(rose.leaf())
print(rose.flower())



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

# Ex2.

class Animal():
    def __init__(self,name ,color):
        self.name=name
        self.color=color
    def about(self):
        return "some information about dog"

class Dog(Animal):

    def about(self):
        return f"{self.name} color is {self.color}"

dog=Dog("picka","Brown")
print(dog.about())

# ex3:
class Parent:
    def __init__(self,house,asset):
        self.house=house
        self.asset=asset
    def parent_asset(self):
        return "The parrent asset"
class Child(Parent):

      def Child_asset(self):
          return f"{self.house}is now child home,{self.asset} is now child car "

child=Child("Home1 ","Car")

print(child.Child_asset())

#
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        return f"Make: {self.make}, Model: {self.model}"
class Car(Vehicle):
    def __init__(self, make, model, number_of_doors):
        super().__init__(make, model)
        self.number_of_doors = number_of_doors

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Number of Doors: {self.number_of_doors}"

my_car = Car("Toyota", "Corolla", 4)
print(my_car.display_info())

# //
class Vahical:
    def __init__(self,make,model,no_of_doors):
        self.make=make
        self.model=model
        self.no_of_doors = no_of_doors
    def display_info(self):
        return f"Make:{self.make},Model:{self.model}"

class Car(Vahical):
    def __init__(self,make,model,no_of_doors):
       super().__init__(make, model,no_of_doors)

    def display_info(self):
        base_info=super().display_info()
        return f"{base_info} Numbers of Doors:{self.no_of_doors}"


car=Car("Toyota","a",4)
print(car.display_info())

# ex4:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Employee ID: {self.employee_id}"
employee = Employee("John Doe", 30, "E12345")
print(employee.display_info())  # Output: Name: John Doe, Age: 30, Employee ID: E12345

# Multiple inheritance
# one child class can inherit from multiple parent classes.
# that allows a class to inherit attributes and methods from more than one parent class.
# This can be useful for combining functionalities from different classes into a single class.
# Method Resolution Order (MRO): The order in which Python looks for a method in the hierarchy of classes.
# Python uses the C3 linearization algorithm to determine the method resolution order.

# Ex1:
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

# ex2
# Combining Functionality from Two Classes
# Let's consider two classes, Walker and Swimmer, and a class Duck that inherits from both
class Walker:
    def walk(self):
        return "Walking"

class Swimmer:
    def swim(self):
        return "Swimming"
class Duck(Walker, Swimmer):
    def quack(self):
        return "Quack!"
duck = Duck()
print(duck.walk())  # Output: Walking
print(duck.swim())  # Output: Swimming
print(duck.quack()) # Output: Quack!

# ex3
# Combining Attributes from Two Classes
# Let's consider two classes, Person and Employee, and a class Manager that inherits from both
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        return f"Name: {self.name}, Age: {self.age}"

class Employee:
    def __init__(self, employee_id, department):
        self.employee_id = employee_id
        self.department = department

    def display_employee_info(self):
        return f"Employee ID: {self.employee_id}, Department: {self.department}"
class Manager(Person, Employee):
    def __init__(self, name, age, employee_id, department):
        Person.__init__(self, name, age)
        Employee.__init__(self, employee_id, department)

    def display_info(self):
        person_info = self.display_person_info()
        employee_info = self.display_employee_info()
        return f"{person_info}, {employee_info}"
manager = Manager("Alice", 40, "E12345", "HR")
print(manager.display_info())


# multiple inheritence without super
class Professor:
    def __init__(self,guidence,schedule):
        self.guidence=guidence
        self.schedule=schedule
    def Prof_things(self):
        return f"Professor: {self.guidence} and {self.schedule}"

class Senior_Teacher:
    def __init__(self,provide_book,provide_lecture):
        self.provide_book=provide_book
        self.provide_lecture=provide_lecture
    def seniors_things(self):
        return f"Seniors: {self.provide_lecture} , {self.provide_book}"

class Junior(Professor,Senior_Teacher):
    def __init__(self,guidence,schedule,provide_book,provide_lecture):
        Professor.__init__(self, guidence,schedule)
        Senior_Teacher.__init__(self, provide_lecture,provide_book)

    def junior_things(self):
        professor_info = self.Prof_things()
        senior_info = self.seniors_things()
        return f"{professor_info},{senior_info}"

junior=Junior("guideline","Schedle","Provide Lecture","lectuuere")
print(junior.junior_things())

# ex4
# creating a class that combines the functionalities of a Flyable and Swimmable
# class for an amphibious vehicle.
class Flyable:
    def fly(self):
        return "Flying"

class Swimmable:
    def swim(self):
        return "Swimming"
class AmphibiousVehicle(Flyable, Swimmable):
    def drive(self):
        return "Driving"
vehicle = AmphibiousVehicle()
print(vehicle.fly())   # Output: Flying
print(vehicle.swim())  # Output: Swimming
print(vehicle.drive()) # Output: Driving

# 3.Multilevel
# Multilevel inheritance allows a class to inherit from another class,
# which is itself derived from another class, forming a chain of inheritance.

# Base Class (Grandparent Class): The topmost class in the hierarchy.
# Intermediate Class (Parent Class): The class that inherits from the base class.
# Derived Class (Child Class): The class that inherits from the intermediate class.
# Chain of Inheritance: The derived class has access to the attributes and methods of all its ancestor classes.
# ex1.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        return f"Name: {self.name}, Age: {self.age}"
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def display_employee_info(self):
        person_info = self.display_person_info()
        return f"{person_info}, Employee ID: {self.employee_id}"
class Manager(Employee):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age, employee_id)
        self.department = department

    def display_manager_info(self):
        employee_info = self.display_employee_info()
        return f"{employee_info}, Department: {self.department}"
manager = Manager("Alice", 40, "E12345", "HR")
print(manager.display_manager_info())


# the Manager class inherits from the Employee class, which in turn inherits from the Person class.
# The Manager class has access to the methods and attributes of both the Employee and Person classes.

# ex2
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_vehicle_info(self):
        return f"Make: {self.make}, Model: {self.model}"
class Car(Vehicle):
    def __init__(self, make, model, number_of_doors):
        super().__init__(make, model)
        self.number_of_doors = number_of_doors

    def display_car_info(self):
        vehicle_info = self.display_vehicle_info()
        return f"{vehicle_info}, Number of Doors: {self.number_of_doors}"
class ElectricCar(Car):
    def __init__(self, make, model, number_of_doors, battery_capacity):
        super().__init__(make, model, number_of_doors)
        self.battery_capacity = battery_capacity

    def display_electric_car_info(self):
        car_info = self.display_car_info()
        return f"{car_info}, Battery Capacity: {self.battery_capacity} kWh"
tesla = ElectricCar("Tesla", "Model S", 4, 100)
print(tesla.display_electric_car_info())
# Output: Make: Tesla, Model: Model S, Number of Doors: 4, Battery Capacity: 100 kWh


# the ElectricCar class inherits from the Car class, which in turn inherits from the Vehicle class.
# The ElectricCar class has access to the methods and attributes of both the Car and Vehicle classes

# Hierarchical inheritance:
# Hierarchical inheritance allows multiple derived classes to inherit from a single base class,
# forming a tree-like structure.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_student_info(self):
        return f"{self.display_info()}, Student ID: {self.student_id}"
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_teacher_info(self):
        return f"{self.display_info()}, Subject: {self.subject}"
student = Student("Alice", 20, "S12345")
print(student.display_student_info())
# Output: Name: Alice, Age: 20, Student ID: S12345

teacher = Teacher("Bob", 40, "Mathematics")
print(teacher.display_teacher_info())

# the Student and Teacher classes both inherit from the Person class.
# They each have additional attributes and methods specific to their roles.

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_vehicle_info(self):
        return f"Make: {self.make}, Model: {self.model}"
class Car(Vehicle):
    def __init__(self, make, model, number_of_doors):
        super().__init__(make, model)
        self.number_of_doors = number_of_doors

    def display_car_info(self):
        return f"{self.display_vehicle_info()}, Number of Doors: {self.number_of_doors}"
class Motorcycle(Vehicle):
    def __init__(self, make, model, type_of_handlebars):
        super().__init__(make, model)
        self.type_of_handlebars = type_of_handlebars

    def display_motorcycle_info(self):
        return f"{self.display_vehicle_info()}, Type of Handlebars: {self.type_of_handlebars}"
car = Car("Toyota", "Camry", 4)
print(car.display_car_info())
# Output: Make: Toyota, Model: Camry, Number of Doors: 4

motorcycle = Motorcycle("Harley-Davidson", "Street 750", "Ape Hangers")
print(motorcycle.display_motorcycle_info())
# ex3
class Animal:
    def __init__(self, species):
        self.species = species

    def display_animal_info(self):
        return f"Species: {self.species}"
class Dog(Animal):
    def __init__(self, species, breed):
        super().__init__(species)
        self.breed = breed

    def display_dog_info(self):
        return f"{self.display_animal_info()}, Breed: {self.breed}"
class Bird(Animal):
    def __init__(self, species, can_fly):
        super().__init__(species)
        self.can_fly = can_fly

    def display_bird_info(self):
        return f"{self.display_animal_info()}, Can Fly: {self.can_fly}"
dog = Dog("Canine", "Golden Retriever")
print(dog.display_dog_info())
# Output: Species: Canine, Breed: Golden Retriever

bird = Bird("Aves", True)
print(bird.display_bird_info())
# the Dog and Bird classes both inherit from the Animal class,
# with their own specific attributes and methods.

# 5.Hybrid

# Hybrid inheritance is a combination of two or more types of inheritance
# combine multiple inheritance with hierarchical inheritance.
# This means it can combine single, multiple, multilevel, and hierarchical inheritance.
# combine multiple inheritance with hierarchical inheritance


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def display_employee_info(self):
        return f"{self.display_info()}, Employee ID: {self.employee_id}"

    class Student(Person):
        def __init__(self, name, age, student_id):
            super().__init__(name, age)
            self.student_id = student_id

        def display_student_info(self):
            return f"{self.display_info()}, Student ID: {self.student_id}"
class TeachingAssistant(Employee, Student):
    def __init__(self, name, age, employee_id, student_id):
        Employee.__init__(self, name, age, employee_id)
        Student.__init__(self, name, age, student_id)

    def display_ta_info(self):
        return f"{self.display_employee_info()}, {self.display_student_info()}"
ta = TeachingAssistant("Alice", 25, "E12345", "S12345")
print(ta.display_ta_info())

print(TeachingAssistant.mro())
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_vehicle_info(self):
        return f"Make: {self.make}, Model: {self.model}"
class Car(Vehicle):
    def __init__(self, make, model, number_of_doors):
        super().__init__(make, model)
        self.number_of_doors = number_of_doors

    def display_car_info(self):
        return f"{self.display_vehicle_info()}, Number of Doors: {self.number_of_doors}"
class Motorcycle(Vehicle):
    def __init__(self, make, model, type_of_handlebars):
        super().__init__(make, model)
        self.type_of_handlebars = type_of_handlebars

    def display_motorcycle_info(self):
        return f"{self.display_vehicle_info()}, Type of Handlebars: {self.type_of_handlebars}"
class ElectricCar(Car):
    def __init__(self, make, model, number_of_doors, battery_capacity):
        super().__init__(make, model, number_of_doors)
        self.battery_capacity = battery_capacity

    def display_electric_car_info(self):
        return f"{self.display_car_info()}, Battery Capacity: {self.battery_capacity} kWh"
electric_car = ElectricCar("Tesla", "Model S", 4, 100)
print(electric_car.display_electric_car_info())

print(ElectricCar.mro())



# with super
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

class A:
    def __init__(self):
        print("A init")
    def jerin(self):
        print("Akter")

class B:
    def __init__(self):
        super().__init__()
        print("B init")

class D(B,A):
    def __init__(self):
        super().__init__()
        super().jerin()
        print("D init")

d=D()


# without super
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



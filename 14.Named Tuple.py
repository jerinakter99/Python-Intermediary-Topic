# A tuple in Python is a built-in data structure it is a useful and efficient way to store an ordered collection of elements in Python,
# especially when you want to ensure that the data remains unchanged throughout the program.

#Immutability: Once a tuple is created, its elements cannot be changed, added, or removed.
#Ordered: Tuples maintain the order of the elements as they are inserted.
#Heterogeneous: Tuples can contain elements of different data types

#Creating Tuples
#create a tuple by placing a comma-separated sequence of values inside parentheses:
# empty tuple
empty_tuple = ()

# tuple with multiple items
my_tuple = (1, "hello", 3.14, True)

# Tuple without parentheses (using commas)
another_tuple = 1, "world", 42

jerin=()
jerin1=(1,"jerin",4.45,True)
jerin2=1,"jerin",True
# access elements in a tuple by using indexing, similar to lists:
print(jerin1[3])
print(jerin2[1])

# Concatenation: You can concatenate two or more tuples using the + operator:
no=( 1,2,4,6)
name=("jerin","jeri","je","ja")
no_name=no+name
print(no_name)

#Namedtuple _ assign meaning to each position in a tuple
#Python supports a type of container dictionary called “namedtuple()” present in the module “collections“
# in tuple we can access  the value by index[] , in named tuple we can access the value with name field,
# more readable and accessible by allowing elements to be accessed by name rather than by index.
#access elements by meaningful names instead of numerical indices.
# Like regular tuples, named tuples are immutable, meaning their values cannot be changed after creation.
# Named tuples are lightweight and efficient, similar to regular tuples,
# but with additional benefits of named fields.
# Named fields provide clarity and self-documentation, making it clear what each element represents.

#namedtuple(typename, field_names)
#typename – The name of the namedtuple.
#field_names – The list of attributes stored in the namedtuple.

from collections import namedtuple

student=namedtuple('student',['id','name','grade']) #declare namedtouple with type name and field name
stu=student(1,'arif',4.5)  # add values

print("student id :",end="")
print(stu[0])           # access values by index

print("student name :", end="")
print(stu.name)         # access values by name
print("s_grade :",end="")
print(stu.grade)






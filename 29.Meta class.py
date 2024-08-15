# A metaclass  is a class of a class. Act as a instance of other class ,
# meta class onno class er instance hisebe kaj kore (assistent programmer)
# metaclass defines the behavior of classes and their instances.
#  A metaclass is just a class thats inherit from type class , the job of the meta class create classes
#A metaclass is just the type of a type or the class of a class
# meta class is a cllass that defines the behavior and structure of other classes
#  its allow you customize class creation and behavior ,its typically used for advanced scenarios
class MyMetaclass(type):
    pass

class A (metaclass=MyMetaclass):
    pass

a=A()
print(f'{type(a)=}')
print(f'{type(A)=}')

# another extremly important property of metaclasses is that ,theey are inherited

class MyMetaclass(type):
    pass

class A (metaclass=MyMetaclass):
    pass
class B(A):


print(f'{A.__class_load=}')
print(f'{type(A)=}')

#
class Meta(type):
    def __new__(self,class_name,bases,attrs):
        return type(class_name,bases,attrs)

class Dog(metaclass=Meta):
    x=5
    y=8
    def hello(self):
        print("Hi")

#attributes are properties associated with objects.
# There are two types of attributes: class level attributes and object level attributes.

# 1.Class Level Attributes

# Class level attributes are attributes that belong to the class itself, not to any specific object of the class.
# They are shared by all objects of the class.
# Class level attributes are defined outside the __init__ method of the class.
# They are accessed using the class name, not the object name.
class MyClass:
    class_attribute = "This is a class attribute"

obj1 = MyClass()
obj2 = MyClass()

print(MyClass.class_attribute)  # Output: This is a class attribute
print(obj1.class_attribute)  # Output: This is a class attribute
print(obj2.class_attribute)  # Output: This is a class attribute

# 2.Object Level Attributes
#
# Object level attributes are attributes that belong to a specific object of the class.
# They are unique to each object and are not shared by other objects of the same class.
# Object level attributes are defined inside the __init__ method of the class.
# They are accessed using the object name, not the class name.
# I have a function I declared a variable this variable is attribute

class MyClass:
    def __init__(self, attribute):
        self.object_attribute = attribute

obj1 = MyClass("Object 1")
obj2 = MyClass("Object 2")

print(obj1.object_attribute)
print(obj2.object_attribute)

# Class level attributes are shared by all objects of the class, while object level attributes are unique to each object.
# Class level attributes are defined outside the __init__ method, while object level attributes are defined inside the __init__ method.
# Class level attributes are accessed using the class name, while object level attributes are accessed using the object name.


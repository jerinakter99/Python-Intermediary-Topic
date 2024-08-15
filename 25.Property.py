# by using property we can save time cz if we run once then it can calculate everthing then we not need
# to rerun again it will give the storing result ,

# Properties in Python allow for the controlled access and modification of an object's attributes.
# You can use the property() function or the @property decorator to define properties.
# Properties enable encapsulation, validation, and the creation of read-only attributes, promoting better design and maintainability of code.
#  They allow you to define methods that are automatically called when you get, set, or delete an attribute.
# This is useful for adding logic when the attribute is accessed or modified, like validation or computing a value on the fly
# fget	Function that returns an attribute’s value (getter method)
# fset	Function that allows you to set an attribute’s value (setter method)



# @property  =  Decorator uesd to define a method as a property(it can be accessed like an attribte)
#               Benefit: Add aditional logic when read ,write , or delete attributes
#               Gives you gatter , setter , deleter method

class Rectangle :
    def __init__(self,width,height):
        self._width=width
        self._height=height
    # //getter method to read
    @property
    def width(self):
        return f"{self._width:.1f}cm"
    @property
    def height(self):
        return f"{self._height:.1f}cm"
    # // setter method to write
    @width.setter
    def width(self,new_width):
        if new_width>0:
            self._width=new_width
        else:
            print("width must be greter than zero")
    @height.setter
    def height(self,new_height):
        if new_height>0:
            self._width=new_height
        else:
            print("height must be greter than zero")
    # //deleter method to delete
    @width.deleter
    def width(self):
        del self._width
        print("width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("hight has been deleted")


rectangle = Rectangle(3,4)
rectangle.width=5
rectangle.height=6
del rectangle.width
del rectangle.height

# print(rectangle.height)
# print(rectangle.width)



# The repr() function  for getting a detailed and unambiguous/clear string representation of an object,
# useful for debugging and logging
class value :
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"value(x={self.x}, y={self.y})"


val = value(2, 3)
print(repr(val))


class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __repr__(self):
        return f"Employee(name='{self.name}', id={self.id})"


emp = Employee("Jeny", 123456)
print(repr(emp))

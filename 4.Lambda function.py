add = lambda x, y: x + y
print(add(2, 3))

#Using Lambda with map
numbers = [1, 2, 3, 4]
squares = map(lambda x: x ** 2, numbers)
print(list(squares))

#Using Lambda with filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name}: {self.age}"

people = [Person("Abir", 20), Person("Arif", 25), Person("Ali", 30)]
sorted_people = sorted(people, key=lambda person: person.age)
print(sorted_people)

#Lambda in the List Comprehensions

numbers = [1, 2, 3, 4, 5, 6]
doubled = [(lambda x: x * 2)(x) for x in numbers]
print(doubled)





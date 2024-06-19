# mutable objects in Python include lists, dictionaries, and sets.
# Mutable objects can be modified

#1.list
my_list = [1, 2, 3]
print(my_list)

my_list[0] = 10
print(my_list)

my_list.append(4)
print(my_list)

#2.Dictonery

my_dict = {"name": "J", "age": 20}
print(my_dict)


my_dict["age"] = 22
print(my_dict)

my_dict["city"] = "Dhaka"
print(my_dict)

#3.Set
my_set = {1, 2, 3}
print(my_set)


my_set.add(4)
print(my_set)


my_set.remove(2)
print(my_set)

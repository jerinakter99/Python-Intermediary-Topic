# List ,Dict
# Python list is an ordered sequence of items.
# built-in data type used to store an ordered collection of items
# Ordered: The elements in a list maintain their order.
# Mutable: You can modify the elements in a list after it has been created.
# Heterogeneous: Lists can contain elements of different data types.

#create list
list=[1,2,3,4,5]
print(list)

1. # reverse a list

list = [100, 200, 300, 400, 500]
list.reverse()
print(list)

# reverse Using negative slicing ,-1 indicates to start from the last item
list = [100, 200, 300, 400, 500]
list = list[::-1]
print(list)

#2.join / concatenate
list1 = ["abir", "jerin", "aham", "hiya", "anas", "arif", ]
list2 = [1, 2, 3, 4, 5]
for list in list2:
    list1.append(list)
print(list1)

# Concatenate two lists index-wise
#Use the zip() function. This function takes two or more iterables (like list, dict, string), aggregates them in a tuple, and returns it

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = [i + j for i, j in zip(list1, list2)]
print(list3)

#3:Turn every item of a list into its square

no = [1, 2, 3, 4]
res = []
for i in no:
    res.append(i * i)

print(res)

4.
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list = [i + j for i in list1 for j in list2]

print(list)

5.
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for i, j in zip(list1, (list2[::-1])):
    print(i, j)


#6 Remove empty strings from the list of strings

no=[1,'',2,3,'']
ab = list(filter(None,no))
print(ab)

# Dictionaries

# in Python are powerful and flexible data structures that allow you to store and manipulate key-value pairs efficiently.
# dictionary is a built-in data type that allows you to store collections of key-value pairs.
# Dictionaries are mutable, which means you can change, add, or remove elements after they have been created
#You can modify, add, or delete key-value pairs.
# create a dictionary using curly braces {} with key-value pairs separated by colons :

dict1={
    'name':"jerin",
    'age':30,
    'hobby':'dance'
}
#access value
print(dict1['name'])
print(dict1['age'])
print(dict1['hobby'])

#modify age
dict1['age']=32
print(dict1['age'])

#add
dict1["siblings"]=3
print(dict1)

#remove
age=dict1.pop('age')
print(dict1)









#string is a sequence of characters
#surrounded by either single quotation marks, or double quotation marks.
print("Hello")
print('Hello')

# create string type variables
name = "Jeny"
print(name)
bio = "I am a trader."
print(bio)

#can access characters in a string using indexing (0-based)
name = "Jerin Akter!"
print(name[0])
print(name[7])

#use slicing to get a substring:
name = "Jerin Akter!"
print(name[0:5])
print(name[6:])
print(name[2:7])

#built-in methods to manipulate strings
name = "  Jerin Akter!  "

# Change case
print(name.upper())
print(name.lower())
print(name.capitalize())

# Strip whitespace
print(name.strip())

# Replace
print(name.replace("Akter", "Maya"))

#several ways to format strings:

#1. join (concatenate) two or more strings
f = "jerin, "
l = "akter"
name = f + l # using + operator
print(name)
#or
name = "jerin"
join = "Hello, " + name + "!"
print(join)
# 2.f-Strings
name = 'Jerin'
dist= 'Narsingdi'

print(f'{name} is from {dist}')
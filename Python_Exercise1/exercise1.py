# Everything in Python is an object, because Python is OOP-oriented

# immutable - it means that everytime I want to change it, it will create a new object in memory.
# mutable - it means that we can change the value or state of the object, without creating a new object.

variable1 = 10
variable2 = 20
variable3 = 20.5

string1 = 'this is my first string'
string2 = "this is my second string"
string3 = f'this is my third string. {variable1}'

print(string3)

string3.capitalize()

# a list is MUTABLE. A string is IMMUTABLE
list1 = [10, 'string2', variable1, string2]
element1 = list[0]
element2 = list[1]
print(f"list1: {list1}")
list1[0] = 3
list1[3] = "test"
print(f"list1: {list1}")
print(list1[0:3:2]) # splicing. Starts at index 0, goes to index 3-1, in steps of 2.

list1.append([1, 2, 3, 4])
list1.append(20)
list1[4].append(5)


# TUPLES - like lists, but are IMMUTABLE, so we cannot change values, but we can extract them

t1 = (1, 2, 'test', list1)
#We can modify the value of a mutable element inside the tuple.
t1[-1].append(20)
print(t1)


# SETS - values are unordered and only UNIQUE values are stored
s1 = {0, 1, 2, 2, 2, 3, 3, 3, 3, 3}
s2 = {4, 5, 3, 2, 2}

print(s1.difference(s2))


# MAPS - stores values in key-value pairs (dictionaries)

d1 = {
    "name": "alex",
    "age": 21,
    "country": "romania"
}
print(d1)
print(d1["name"])
print(d1["age"])

k = list(d1.keys())

# logical operators 
# and, or, not
# <, >, <=, >=, ==, !=
# True, False

if (variable1 == variable2):
    print("They are equal")
elif (variable1 == variable3):
    print("variable1 and variable3 are equal")
else:
    print("They are not equal")
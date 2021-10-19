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



#LOOPS

#FOR loop

l1 = [1, 2, 3, 4]
for elem in l1:
    a = elem ** 3
    print(a)

print("Done!")

for i, e in enumerate(l1):  # i = index, e = element
    if i > 2:
        print(i, e)

s = 0
for i in range(0, 100):
    s = s + 1

print(f"Average of first 99 numbers is: {s/99}")


#WHILE loop

n = 0
while n < 2 or n > 10:
    print("Please enter a number between 2 and 10")
    n = int(input())

print("Done!")


#FUNCTIONS

def sum_numbers(n, p=0):
    s = 0
    for i in range(0, n):
        s = s + i
    print(f"Sum of the first {n-1} numbers is {s}")
    return s

def sum_numbers_raised(n, p=2):
    s = 0
    for i in range(0, n):
        s = s + i ** p
    print(f"Sum of the first {n-1} numbers raised to the power of {p} is {s}")
    return s

a = sum_numbers(10)
b = sum_numbers(n=20, p=100)

function_label = sum_numbers # we store our function in a variable
function_label(10)

l = [sum_numbers, sum_numbers_raised]

for f in l:
    f(10)


def power(a, b):
    return a ** b

def sum_numbers_raised_to_power(n, p, power):
    s = 0
    for i in range(0, n):
        s = s + power(i, p)
    print(f"Sum of the first {n-1} numbers raised to the power of {p} is {s}")
    return s

sum_numbers_raised_to_power(10, 2, power)


#DECORATORS - modifies a function without touching the body of the function

import datetime
# or, instead of importing the whole library: from datetime.datetime import now

def my_decorator(func):
    def wrapper():
        print("This is happening before we call func")
        if (datetime.datetime.now().hour <= 22):
            func()
        else:
            print("Everyone is sleeping. Leave me alone")
        print("This is happening after we call func")
    return wrapper

#We can use decorators like this
@my_decorator
def hello():
    print("Hello World!")

hello()
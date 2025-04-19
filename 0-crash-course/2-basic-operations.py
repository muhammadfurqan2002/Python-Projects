import math


x = 10
y = 5

print(x-y)
print(x+y)
print(x*y)
print(x/y)
print(x % y)
print(x**y)

"""

multi line comments

"""

x += 15
x = x+15


print(x)


first_name = "John"
last_name = "Doe"
full_name = first_name + " "+last_name

print(full_name)

print("Hey my name is "+first_name+" and last name is "+last_name)

# f strings (*imp*)
print(f"Hey my name is {first_name} and last name is {last_name}")

# int floor division

a = 17
b = 5

print(a/b)
print(a//b)  # it round down the value to the nearest integer


i, j, k = 1, 2, 3
print(i, j, k)

# swap values

m = 20
n = 10
m, n = n, m

print(m, n)


# comparison operator

c = 5
d = 10
print(c == d)
print(c != d)
print(c >= d)
print(c <= d)
print(c < d)
print(c > d)


# logical operators

a = True
b = False
print(a and b)
print(a or b)
print(not b)

# string operations

text = "Python programming"

print(text[0:6])
print(text[7:])
print(text[::-1])  # reverse the string

# String formatting with .format()
name = "alice"
age = 25
msg = "my name is {} and i am {} years old".format(name, age)
print(msg)

# Using placeholders
msg2 = "My name is {0} and I am {1} years. {0} is a nice name".format(
    name, age)
print(msg2)


# Math module operations

print(math.pi)
print(math.sqrt(2))
print(math.floor(17.8))
print(math.ceil(17.8))
print(math.pow(2, 3))
print(round(math.pi, 2))

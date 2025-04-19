# For loop


print("For loop 1 to 5:")
for i in range(1, 6):
    print(i)


print("/n Reverse for loop 5 to 1:")
for i in range(5, 0, -1):
    print(i)


# while loop
print("/n While loop 1 to 5:")
i = 1
while i <= 5:
    print(i)
    i += 1


#  looping through list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


# Reverse the fruit list

for fruit in reversed(fruits):
    print(fruit)


#  loop with enumerate

print("FRUIT WITH INDICES")
for i, fruit in enumerate(fruits):
    print(f"{i}-{fruit}")

# loop with dictionaries
person = {
    "name": "John",
    "age": "21",
    "city": "New York",
}

for key, value in person.items():
    print(f"{key}-{value}")


# List comprehension (compact loop for creating list)

squares = [x**2 for x in range(1, 6)]
print("squares of 1 to 5 ", squares)

# For loop with zip() - use to iterate multiple lists in parallel
color = ["red", "yellow", "green"]
print("\n Fruits and their colors")

for fruit, color in zip(fruits, color):
    print(f"{fruit}-{color}")


# Break and continue

for i in range(1, 10):
    if i > 5:
        break
    print(i)


for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i)


# infinite loops with break condition
i = 1
while True:
    print(i)
    if (i > 5):
        break
    i += 1

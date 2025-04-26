# Lists are collections of items that can be of any data type, including strings, integers, floats, and other lists

numbers = [1, 2, 3, 4, 5, 6, "Heloo", True]

print(numbers[6])


numbers[1] = "dummy"
numbers.append(56)
numbers.remove(3)

print(numbers)

# slicing

numbers = [1, 2, 3, 4, 5]
print(numbers[1:3])  # elements from index 1 to 3
print(numbers[::3])  # every other element
print(numbers[::-1])  # reverse array
print(numbers+[7, 8, 9, 10])  # concat into array
print(numbers*2)  # repeat the list


# Dictionaries are collections thath store data as key-value pairs


student = {
    "name": "Emma",
    "age": 25,
    "courses": ["Math", "Science", "Computer Science"]
}
print(student["courses"])

student["grade"] = "A+"
student["age"] += 10

print(student.keys())
print(student.items())
print(student.values())


for key, value in student.items():
    print(f"{key}:{value}")


# Sets are unordered collections of unique items-no duplicate allowed


unique_colors = {"red", "green", "blue", "red"}
print("unique colors", unique_colors)


# tuples are ordered collections that cannot be changes after creation

coordinates = (10.5, 20.8)

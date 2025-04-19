temp = 28

if temp > 30:
    print("It's hot outside")
elif temp < 30:
    print("It's sunny day")
else:
    print("It's not hot outside")


age = 25
has_license = True
if age >= 18 and has_license:
    print("You can drive")
elif age >= 18 and not has_license:
    print("You can drive but you need a license")
else:
    print("You can't drive")


# Nested if statements
score = 85

if score >= 60:
    print("You passed")
    if score > 90:
        print("You did great and got A+")
    elif score > 80:
        print("You did great and got A")
    elif score > 70:
        print("You did great and got B")
    else:
        print("You did great and got C")
else:
    print("You failed")
    if score < 50:
        print("You need to study more")
    else:
        print("You need to practice more")


#  using the "in" operator with conditionals
fruit = "apple"

if fruit in ["apple", "banana", "orange"]:
    print(f"{fruit} is a fruit and present in list")


# Ternary operator

age = 25
status = "adult" if age >= 18 else "minor"
print(f"You are an {status}")


password = "12345"
if password == "12345":
    print("Access granted")
else:
    print("Access denied")


# chaining comparisons
# This is a common pattern in Python and can be used to check if a value is within a range.

x = 10
y = 20
z = 15
if x < z < y:
    print(f"{z} is between {x} and {y}")


# truty or falsy values

user_input = ""
if user_input:
    print("User input is not empty")
else:
    print("User input is empty")

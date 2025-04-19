name = input("what's your name?")
print("hello", name)

age = input("how old are you?")
years_to_100 = 100 - int(age)
print(f"you will be 100 in {years_to_100} years")

height = float(input("how tall are you in meters?"))
print(f"your height is {height} meters")


x, y = input("enter two numbers separated by a space: ").split()

print(f"x: {x}, y: {y}")

user_choice = input("Choose a color (or press Enter for default)")
if user_choice == "":
    user_choice = "blue"
print(f"Your choice is {user_choice}")

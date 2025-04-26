# functions in python

def greet_everyone():
    print("heleoo everyone")


greet_everyone()
greet_everyone()


def greet(name):
    print(f'Heleo {name}')


greet("furqan")


def greet_user(name):
    print("Heloo,", name, "welcome to our app")
    print("we hope you enjoy using our services")
    print("Let us know if you need any help.\n")


greet_user("furqan")
greet_user("abdulrehman")
greet_user("muneeb")
greet_user("haseeb")


def power(base, exponent):
    return base**exponent


x = power(2, 2)
y = power(2, 3)
z = power(2, 4)
print(x, y, z)

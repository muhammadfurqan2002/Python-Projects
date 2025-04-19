print("hello world")

name = "furqan"
age = 45
height = 5.9
is_student = True

print("Hey my name is "+name)
print("I am ", age, " years old")

print(name[0:3])

message = "hello World"
print(message.upper())
print(message.lower())
print(message.capitalize())
print(message.replace('l', 'L'))

# python is case sensitive language

print("World" in message)
print(len(message))

greeting1 = "hello"
greeting2 = "Hello"

if greeting1 == greeting2:
    print("equal")
else:
    print("not equal")


# Type conversion

age_str = "30"
age_num = int(age_str)
print(type(age_num))
print(type(age_str))


price_float = 29.99
price_int = int(price_float)
print(type(type(price_int)))
print(type(price_float))

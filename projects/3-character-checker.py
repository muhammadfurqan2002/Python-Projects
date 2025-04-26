print("Character Checker")
text = input("Enter a character")


if text.isalpha():
    print("This is character")
elif text.isdigit():
    print("This is digit")
else:
    print("Unknown")

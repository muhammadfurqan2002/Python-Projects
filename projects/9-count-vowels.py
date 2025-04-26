print("VOWELS COUNTER")

# while True:
#     text = input("Enter some text (or 'quit'): ")
#     vowel_count = 0
#     if text.lower() == "quit":
#         print("😜 Goodbye!")
#         break
#     for letter in text:
#         if letter.lower() in ["a", "e", "i", "o", "u"]:
#             vowel_count += 1
#     print(f"That text has {vowel_count} vowels!")


while True:
    text = input("Enter some text (or 'quit'): ")

    if text.lower() == "quit":
        print("😜 Goodbye!")
        break
    vowels = sum(1 for char in text.lower() if char in "aeiou")
    print(f"That text has {vowels} vowels!")

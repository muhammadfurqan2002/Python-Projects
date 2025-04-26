import random

print("WORD SCRAMBLER")
while True:
    word = input("Enter a word to scramble (or 'quit'): ")
    if word.lower() == "quit":
        print("GoodBye")
        break
    letters = list(word)
    random.shuffle(letters)
    print(f"Scrambled: {"".join(letters)}")

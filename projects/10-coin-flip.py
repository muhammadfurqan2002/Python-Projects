import random
print("Coin Flip Game")
print("Guess head or tails")

while True:

    text = input("Enter your guess (heads/tails): ").lower()
    if text != "heads" and text != "tails":
        print("Please enter, 'heads' or 'tails")
        continue
    flip = random.choice(["heads", "tails"])

    if flip == text:
        print("You Guess Correctly")
    else:
        print("Sorry, wrong guess")
    again = input("Want to play again (y/n): ")
    if again == "n":
        break

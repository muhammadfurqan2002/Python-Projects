import random
import datetime
import os
import time
import sys


random_number = random.randint(1, 10)
print(f"Random number is {random_number}")


# choose a random element from list
fruits = ["apple", "orange", "cherry", "banana"]
random_fruit = random.choice(fruits)
print(random_fruit)

# shuffle list
random.shuffle(fruits)

print(f"Shuffle list is :", fruits)


curret_date = datetime.datetime.now()
print(curret_date)
print(datetime.date.today())
print(datetime.date.today().year)


current_directory = os.getcwd()
print(current_directory)
print(os.listdir('.'))


print("Waiting for 1 seconds...")
time.sleep(1)
print("Done!")

# System module
print("system version", sys.version)

import random
first_parts = ["Sky", "Star", "Moon", "Sun", "Fire", "Ice"]
last_parts = ["rider", "walker", "seeker", "keeper", "singer", "Ice"]

print("Name Generator")

count = int(input("How many names do you want?"))
# for i in range(count):
for _ in range(count):
    first_name = random.choice(first_parts)
    last_name = random.choice(last_parts)

    print(f"{first_name}{last_name}")

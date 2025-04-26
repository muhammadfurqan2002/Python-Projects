print("🏃‍♀️ STEP COUNTER 🏃‍♀️")
daily_goal = int(input("What is you daily step goal:"))
step_taken = int(input("How many steps have you taken:"))

steps_count = daily_goal-step_taken

if step_taken > 0:
    print(f"You need {steps_count} more steps to reach your goal!")
elif steps_count < 0:
    print(f"Congratulations! You've exceeded you goal by {steps_count} steps!")
else:
    print("Congratulations! You've completed your goal")

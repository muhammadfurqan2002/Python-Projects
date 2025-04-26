print("Grade Calculator")
scores = []
isTrue = True
while isTrue:
    marks = input("Enter a test score (or 'done')")

    if marks.lower() == "done":
        isTrue = False
        print("You are done")
    else:

        scores.append(float(marks))
        average = sum(scores) / len(scores)
        print(f"Average score:{average:.1f}")
        if average >= 90:
            print("Grade:A")
        elif average >= 80:
            print("Grade:B")
        elif average >= 60:
            print("Grade:c")
        else:
            print("Fail")

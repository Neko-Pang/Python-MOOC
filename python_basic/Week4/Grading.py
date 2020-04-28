# Grading.py
score = eval(input("Please type in your score in 100: "))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "E"
print("Your grade is: {}".format(grade))

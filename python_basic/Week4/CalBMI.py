# CalBMI.py
height, weight = eval(input("Please type in your height(meter) and weight(kg)(separate with \",\"): "))
bmi = weight / pow(height, 2)
print("Your BMI is: {:.2f}".format(bmi))
who, nat = "", ""
if bmi < 18.5:
    who, nat = "underweight", "underweight"
elif 18.5 <= bmi < 24:
    who, nat = "normal", "normal"
elif 24 <= bmi < 25:
    who, nat = "normal", "overweight"
elif 25 <= bmi < 28:
    who, nat = "overweight", "overweight"
elif 28 <= bmi < 30:
    who, nat = "overweight", "obese"
elif bmi >= 30:
    who, nat = "obese", "obese"
else:
    print("WTF is happening?")
    exit()
print("WHO bmi: " + who + " " + "NAT bmi: " + nat)

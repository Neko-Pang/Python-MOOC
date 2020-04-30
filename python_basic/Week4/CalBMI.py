# CalBMI.py
height, weight = eval(input("Please type in your height(meter) and weight(kg)(separate with \",\"): "))
bmi = weight / pow(height, 2)
print("Your BMI is: {:.2f}".format(bmi))
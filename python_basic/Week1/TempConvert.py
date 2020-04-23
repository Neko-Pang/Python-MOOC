#TempConvert.py
def printResult(x, y):
    print("The converted temperature is {:.2f} ".format(x) + y + "°")

TempStr = input("Plz type in the temperature value with C or F:  ")
if (TempStr[-2] in ['F', 'f']) & (TempStr[-1] in ['A', 'a']):
    C = (eval(TempStr[0:-2]) - 32) / 1.8
    # print("The converted temperature is {:.2f}".format(C))
    printResult(C, "C")
elif TempStr[-1] in ['F', 'f']:
    C = (eval(TempStr[0:-1]) - 32) / 1.8
    printResult(C, "C") 
elif (TempStr[-2] in ['C', 'c']) & (TempStr[-1] in ['E', 'e']):
    F = 1.8 * eval(TempStr[0:-2]) + 32
    printResult(F, "F")
elif TempStr[-1] in ['C', 'c']:
    F = 1.8 * eval(TempStr[0:-1]) + 32
    printResult(F, "F")
    # print("The converted temperature is {:.2f}F".format(F))
else:
    print("Format ERROR")

# eval('print("Hello")')

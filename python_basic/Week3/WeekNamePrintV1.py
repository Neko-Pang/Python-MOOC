# WeekNamePrintV1.py
weekStr = "MonTueWedThuFriSatSun"
weekID = eval(input("Please type in the sequence number of the day: "))
if (weekID <= 7) and (weekID > 0):
    pos = (weekID - 1) * 3
else:
    print("number is not valid")
    exit()
print(weekStr[pos:pos + 3])
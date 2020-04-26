# WeekNamePrintV2.py
weekStr = "一二三四五六日"
weekID = eval(input("请输入星期数字(1-7)"))
if (weekID <= 7) and (weekID > 0):
    weekStr = "星期"  + weekStr[weekID - 1]
    print(weekStr)
else:
    print("星期数字有误！")

# StringHandeling.py
str = "AbCdEfGh"
print("Original: " + str)
str = str.upper()
print("After upper: " + str)
str = str.lower()
print("After lower: " + str)
str = "A,B,C"
strSplited = str.split(",")
print(strSplited)
str = "an a apple a day"
strCount = str.count("a")
print(str + ": a * ", strCount)
str = "QwQ"
str = str.replace("Q", "T")
print(str)
print(str.center(20, "="))
str = "abc de QwQ ed cba"
print(str.strip("abcd "))
str = "~".join("12345")
print(str)
print("{}:计算机{}的CPU占用率为{}%".format("2018-10-10", "C", 10))
print ("{0:=^20}".format("ABCDE"))
print("{0:b}, {0:c}, {0:d}, {0:o}, {0:x}, {0:X}".format(425))
print("{0:e}, {0:E}, {0:f}, {0:%}".format(3.14))
array = [0,1,2,3,4,5,6,7,8,9]
# print(array[1:-1:3])
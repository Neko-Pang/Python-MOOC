# TextProBarV1.py
import time
scale = 10
print("start processing".center(10, "-"))
for i in range(scale + 1):
    a = "*" * i
    b = "." * (scale - i)
    c = (i / scale) * 100
    print("{0:^3.0f}%[{1}->{2}]".format(c, a, b))
    time.sleep(0.1)
print("stop processing".center(10, "-"))
# print("start processing".center(10, "-"))
# for i in range (101):
#     print("\r{:3}%".format(i), end = "")
#     time.sleep(0.1)
# print("\nstop processing".center(10, "-"))
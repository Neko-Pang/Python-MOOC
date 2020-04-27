# TextProbarV2.py
import time
print("start processing".center(10, "-"))
for i in range (101):
    print("\r{:3}%".format(i), end = "")
    time.sleep(0.1)
print("\nstop processing".center(10, "-"))
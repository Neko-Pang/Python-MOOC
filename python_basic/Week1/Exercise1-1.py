# Exercise1-1.py
c = eval(input())
s = "Hello World"
if(c == 0):
    print(s)
elif(c > 0):
    x = 0
    while(x < len(s)-1):
        print(s[x]+s[x+1])
        x += 2
    if(len(s)-x > 0):
        print(s[-1])
elif(c < 0):
    for y in s:
        print(y)
else:
    print("error")

# Official Answer
# n = eval(input())
# if n == 0:
#     print("Hello World")
# elif n > 0:
#     print("He\nll\no \nWo\nrl\nd")
# else:
#     for c in "Hello World":
#         print(c)
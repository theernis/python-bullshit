import time
x = float(input("number: "))
y = float(input("power: "))
def math(a, b):
    print(a)
    if not(b == 0):
        math(a*x, b-1)
    else:
        while(0 == 0):
            time.sleep(1)
math(x, y-1)
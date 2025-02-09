import math

def getFact():
    n = 0
    while True:
        yield math.factorial(n)
        n += 1

number = getFact()
n = 5
for i in range(n + 1):
    print(next(number))
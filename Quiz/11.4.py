def getInf():
    n = 2
    while True:
        yield n
        n += 2

numbers = getInf()
for i in range(10):
    print(next(numbers))
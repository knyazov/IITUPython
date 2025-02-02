def sum_integers(a, b):
    sum = 0
    for i in range(abs(a), abs(b)):
        sum += i
    print(sum)


a, b = map(int, input().split())
sum_integers(a, b)

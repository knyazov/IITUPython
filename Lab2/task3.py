def fibonacci_num(n):
    if n <= 1:
        return n
    else:
        return fibonacci_num(n - 1) + fibonacci_num(n - 2)


n = int(input())
if n <= 0:
    print("Enter numbers greater than 0")
else:
    k = 0
    for i in range(1, n + 1):
        print(fibonacci_num(i), end=" ")

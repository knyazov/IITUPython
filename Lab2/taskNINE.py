def fibonacci_num(n):
    if n <= 1:
        return n
    else:
        return fibonacci_num(n - 1) + fibonacci_num(n - 2)


n = int(input())
array = []
if n <= 0:
    print("Enter numbers greater than 0")
else:
    k = 0
    for i in range(0, n):
        array.append(fibonacci_num(i))

print(array)

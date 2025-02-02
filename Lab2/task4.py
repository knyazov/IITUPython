def sequence(n):
    if n <= 0:
        return n
    else:
        print(n, end=" ")
        return sequence(n - 5)


n = int(input())
sequence(n)

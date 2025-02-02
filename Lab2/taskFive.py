def extraNumber(a, b, c):
    number = 0
    if a == b:
        number = c
    elif a == c:
        number = b
    else:
        number = a
    print(f"extraNumber (a, b, c) = {number}")


a, b, c = map(int, input().split())
extraNumber(a, b, c)
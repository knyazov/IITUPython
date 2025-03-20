def tenBa(text):
    a = 0
    b = 0
    for i in range(len(text)):
        ch = ""
        ch = text[i]
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'y':
            a += 1
        elif ch.isalpha():
            b += 1
    return a == b
text = input()
print(tenBa(text.lower()))